require('dotenv/config');
const express = require('express');
const s3Routes = require('./src/routes/s3Routes')
const userRoutes = require('./src/routes/userRoutes')

const app = express();
//const HOSTNAME = "::"
const PORT = process.env.PORT || 4001;

app.use('/users', userRoutes)
app.use('/objects', s3Routes)

app.listen(PORT, "127.0.0.1", () => {
    console.log("Server is up at ", PORT);
})
