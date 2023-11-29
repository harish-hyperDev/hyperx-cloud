const multer = require('multer');
const AWS = require('aws-sdk');
const { S3Client } = require("@aws-sdk/client-s3");


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

module.exports = {
    client,
    s3,
    upload
}

