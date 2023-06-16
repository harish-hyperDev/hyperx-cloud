import boto3
import wasabi.config as Config


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Use the following code to connect using Wasabi profile from .wsb/credentials file
session = boto3.Session(profile_name="wasabi")
credentials = session.get_credentials()
wsb_access_key_id = Config.WSB_ACCESS_KEY_ID  
wsb_secret_access_key = Config.WSB_SECRET_ACCESS_KEY

s3 = boto3.client(  's3',
                    endpoint_url = Config.WSB_S3_CUSTOM_DOMAIN,  #'https://s3.wasabisys.com',
                    aws_access_key_id = wsb_access_key_id,
                    aws_secret_access_key = wsb_secret_access_key)

uri = f"mongodb+srv://atlas:{Config.MONGO_URI_PASS}@primary-test-cluster.xylx7ly.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


