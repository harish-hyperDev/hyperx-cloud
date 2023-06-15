# sarvendriya na nayanam pramaanam
from fastapi import FastAPI
import wasabi.config as Config
from django.http import JsonResponse

import pprint
import json
import boto3, botocore

app = FastAPI()

# Use the following code to connect using Wasabi profile from .aws/credentials file
session = boto3.Session(profile_name="wasabi")
credentials = session.get_credentials()
aws_access_key_id = Config.WSB_ACCESS_KEY_ID  
aws_secret_access_key = Config.WSB_SECRET_ACCESS_KEY

s3 = boto3.client(  's3',
                    endpoint_url= Config.WSB_S3_CUSTOM_DOMAIN,  #'https://s3.wasabisys.com',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

@app.get("/get")
async def getAllObjects():
    objects = s3.list_objects_v2(Bucket=Config.WSB_STORAGE_BUCKET_NAME)
    # return {"Contents": objects['Contents']}
    return JsonResponse(objects)

@app.post("/post/{object_name}")
async def uploadObject():
    file_path = "<file-to-upload>"
    key_name = "<key-name>"
    
    print(Config.WSB_ACCESS_KEY_ID)
    # all_items = s3.get_object(Bucket=bucket_name)
    # pp(all_items)

    return {"message": "POST"}



@app.get("/download/{object_key}")
async def downloadObject(object_key):
    
    # KEY = 'users.ico'
    try:
        s3.download_file(Config.WSB_STORAGE_BUCKET_NAME, object_key, object_key) #.download_file(KEY, 'my_local_users.ico')
        
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise