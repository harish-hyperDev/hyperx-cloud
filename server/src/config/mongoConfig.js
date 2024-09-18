require('dotenv/config');
const mongoose = require('mongoose')

const uri = `mongodb+srv://${process.env.MONGO_URI_USERNAME}:${process.env.MONGO_URI_PASS}@freeclusterm0.ezw3y.mongodb.net/${process.env.MONGO_DB_NAME}?retryWrites=true&w=majority;`
