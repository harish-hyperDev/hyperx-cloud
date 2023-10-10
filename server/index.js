require('dotenv/config');
const express = require('express');
const multer = require('multer');
const AWS = require('aws-sdk');
const { GetObjectCommand, S3Client, ListObjectsV2Command } = require("@aws-sdk/client-s3");
const { uuid } = require('uuidv4');

const app = express();
const PORT = process.env.PORT || 4400;

const credentials = {
    accessKeyId: process.env.WSB_ID,
    secretAccessKey: process.env.WSB_SECRET,
}

const endpoint = new AWS.Endpoint('https://s3.ap-southeast-1.wasabisys.com');
const s3 = new AWS.S3({
    credentials,
    endpoint: endpoint
})

const client = new S3Client({
    region: 'ap-southeast-1',
    credentials,
    endpoint: endpoint,
})

const storage = multer.memoryStorage({
    destination: function(req, file, callback) {
        callback(null, '')
    }
})

const upload = multer({storage}).single('file')

async function listContents() {
    // https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/interfaces/listobjectsv2commandinput.html
    const input = {
        Bucket: process.env.WSB_BUCKET_NAME
    }

    // https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/classes/command.html
    const cmd = new ListObjectsV2Command(input)
    // console.log(cmd)
    
    /* const command = new GetObjectCommand({
        Bucket: process.env.WSB_BUCKET_NAME,
        Key: "*"
    }) */
    
    // https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/classes/listobjectsv2command.html
    return await client.send(cmd)
}

app.get('/', async (req,res) => {
    
    try {
        // const response = await client.send(command);
        const response = await listContents();
        const contents = await response.Contents;
        
        res.json({
            bucketObjects: contents
        })
    } catch (err) {
        // console.log(err)
        res.json({
            error: err
        })
    }
})

app.get('/download', (req,res) => {
   
    var fileKey = req.query['fileKey'];

    console.log('Trying to download file', fileKey);
    var options = {
        Bucket: process.env.WSB_BUCKET_NAME,
        Key: fileKey,
    };

    res.attachment(fileKey);
    var fileStream = s3.getObject(options).createReadStream();
    fileStream.pipe(res);
})

app.post('/upload', upload, (req,res) => {
    // console.log(req.file);
    let myFile = req.file.originalname.split(".");
    const fileType = myFile[myFile.length - 1]

    const params = {
        Bucket: process.env.WSB_BUCKET_NAME,
        Key: `${uuid()}.${fileType}`,
        Body: req.file.buffer
    }
    s3.upload(params, (error, data) => {
        if (error)
            res.status(500).send(error)
        
        res.status(200).send(data)
    })
})

app.listen(PORT, () => {
    console.log("Server is up at ", PORT);
})