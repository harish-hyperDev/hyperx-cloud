require('dotenv/config');
const express = require('express');
const multer = require('multer');
const AWS = require('aws-sdk');
const { uuid } = require('uuidv4');

const app = express();
const PORT = process.env.PORT || 4400;

const ep = new AWS.Endpoint('https://s3.ap-southeast-1.wasabisys.com');
const s3 = new AWS.S3({
    accessKeyId: process.env.WSB_ID,
    secretAccessKey: process.env.WSB_SECRET,
    endpoint: ep
})

const storage = multer.memoryStorage({
    destination: function(req, file, callback) {
        callback(null, '')
    }
})

const upload = multer({storage}).single('image')

app.post('/upload', upload, (req,res) => {
    // console.log(req.file);
    let myFile = req.file.originalname.split(".");
    const fileType = myFile[myFile.length - 1]

    /* res.send({
        message: "Hello"
    }) */

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
