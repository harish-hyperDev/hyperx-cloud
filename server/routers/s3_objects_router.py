from fastapi import APIRouter, Depends, HTTPException
from botocore.exceptions import ClientError

from helpers.loaders import s3 as s3_client
import helpers.config as Config
import botocore


router = APIRouter(
    prefix="/objects",
    tags=["objects"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_all_objects():
    objects = s3_client.list_objects_v2(Bucket=Config.WSB_STORAGE_BUCKET_NAME)
    return {"Objects" : objects['Contents']}


@router.post("/")
async def upload_object(file_object):
    file_path = "<file-to-upload>"
    key_name = file_object
    
    try:
        response = s3_client.upload_file(file_object, Config.WSB_STORAGE_BUCKET_NAME, file_object.filename)
        print(response)
    except ClientError as e:
        return False
    return True


@router.get("/download/{object_key}")
async def download_object(object_key):
    try:
        s3_client.download_file(Config.WSB_STORAGE_BUCKET_NAME, object_key, object_key)    #.download_file(KEY, 'my_local_users.ico')
        
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    