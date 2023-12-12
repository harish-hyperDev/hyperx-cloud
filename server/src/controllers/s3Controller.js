const { ListObjectsV2Command } = require("@aws-sdk/client-s3");
const { uuid } = require('uuidv4');
const { client } = require('../config/s3')

async function listContents() {
    const input = {
        Bucket: process.env.WSB_BUCKET_NAME
    }

    const cmd = new ListObjectsV2Command(input)

    /* const command = new GetObjectCommand({
        Bucket: process.env.WSB_BUCKET_NAME,
        Key: "*"
    }) */

    return await client.send(cmd)
}

const getObjects = async (req, res) => {
    

    try {
        // const response = await client.send(command);
        const response = await listContents();
        res.json({ bucketObjects: response.Contents })

    } catch (err) {
        res.json({ error: err })
    }
}

const downloadObject = (req, res) => {

    var fileKey = req.query['fileKey'];

    console.log('Trying to download file', fileKey);
    var options = {
        Bucket: process.env.WSB_BUCKET_NAME,
        Key: fileKey,
    };

    res.attachment(fileKey);
    var fileStream = s3.getObject(options).createReadStream();
    fileStream.pipe(res);
}

const uploadObject = (req, res) => {

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
}

module.exports = {
    getObjects,
    downloadObject,
    uploadObject
}
