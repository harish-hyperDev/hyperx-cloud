from fastapi import APIRouter, Depends, HTTPException

from helpers.loaders import s3
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
    objects = s3.list_objects_v2(Bucket=Config.WSB_STORAGE_BUCKET_NAME)
    return {"Objects" : objects['Contents']}


@router.post("/{object_name}")
async def upload_object():
    file_path = "<file-to-upload>"
    key_name = "<key-name>"
    
    print(Config.WSB_ACCESS_KEY_ID)
    # all_items = s3.get_object(Bucket=bucket_name)

    return {"message": "POST"}


@router.get("/download/{object_key}")
async def download_object(object_key):
    try:
        s3.download_file(Config.WSB_STORAGE_BUCKET_NAME, object_key, object_key)    #.download_file(KEY, 'my_local_users.ico')
        
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    