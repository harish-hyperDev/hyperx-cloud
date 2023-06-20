from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import boto3
import helpers.config as Config


# Use the following code to connect using Wasabi profile from .wsb/credentials file
session = boto3.Session(profile_name="wasabi")
credentials = session.get_credentials()

s3 = boto3.client(  's3',
                    endpoint_url = Config.WSB_S3_CUSTOM_DOMAIN,  #'https://s3.wasabisys.com',
                    aws_access_key_id = Config.WSB_ACCESS_KEY_ID,
                    aws_secret_access_key = Config.WSB_SECRET_ACCESS_KEY)

uri = f"mongodb+srv://{Config.MONGO_URI_UNAME}:{Config.MONGO_URI_PASS}@primary-test-cluster.xylx7ly.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
MonogDBClient = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    MonogDBClient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


