require('dotenv/config');
const express = require('express');
const s3Routes = require('./src/routes/s3Routes')

const app = express();
const PORT = process.env.PORT || 5500;

app.use('/objects', s3Routes)

app.listen(PORT, () => {
    console.log("Server is up at ", PORT);
})