from fastapi import FastAPI
import wasabi.config as Config
from wasabi.loaders import s3, client
import botocore


app = FastAPI()


@app.get("/get")
async def getAllObjects():
    objects = s3.list_objects_v2(Bucket=Config.WSB_STORAGE_BUCKET_NAME)
    # return {"Contents": objects['Contents']}
    return {"Objects" : objects['Contents']}


@app.get("/post/{object_name}")
async def uploadObject():
    file_path = "<file-to-upload>"
    key_name = "<key-name>"
    
    print(Config.WSB_ACCESS_KEY_ID)
    # all_items = s3.get_object(Bucket=bucket_name)
    # pp(all_items)

    return {"message": "POST"}


@app.get("/download/{object_key}")
async def downloadObject(object_key):
    try:
        s3.download_file(Config.WSB_STORAGE_BUCKET_NAME, object_key, object_key)    #.download_file(KEY, 'my_local_users.ico')
        
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
        
        
@app.get('/db')
async def get_db():
    db = client["HyperWasabi"]
    db_col = db['User']
    return { "db": db.list_collection_names() }