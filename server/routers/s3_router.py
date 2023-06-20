from fastapi import APIRouter, Depends, HTTPException

from helpers.loaders import s3
import helpers.config as Config
import botocore


router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/get")
async def getAllObjects():
    objects = s3.list_objects_v2(Bucket=Config.WSB_STORAGE_BUCKET_NAME)
    # return {"Contents": objects['Contents']}
    return {"Objects" : objects['Contents']}


@router.get("/post/{object_name}")
async def uploadObject():
    file_path = "<file-to-upload>"
    key_name = "<key-name>"
    
    print(Config.WSB_ACCESS_KEY_ID)
    # all_items = s3.get_object(Bucket=bucket_name)
    # pp(all_items)

    return {"message": "POST"}


@router.get("/download/{object_key}")
async def downloadObject(object_key):
    try:
        s3.download_file(Config.WSB_STORAGE_BUCKET_NAME, object_key, object_key)    #.download_file(KEY, 'my_local_users.ico')
        
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    