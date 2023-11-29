const express = require('express')
const router = express.Router()

const { upload } = require('../config/s3')
const { getObjects, downloadObject, uploadObject } = require('../controllers/s3Controller')

router.get('/', getObjects)
router.get('/download', downloadObject)
router.post('/upload', upload, uploadObject)

module.exports = router