from fastapi import APIRouter, Depends, Response, status, Form, File, UploadFile
from typing_extensions import Annotated
from django.http import JsonResponse
from bson import json_util
from uuid import uuid4
from botocore.exceptions import ClientError

from helpers.db_config import db
from actions.UserActions import UserActions
from actions.UserObjectActions import UserObjectActions
from models.model import UserModel, FileUploadModel


from helpers.loaders import s3 as s3_client
import helpers.config as Config
import io

from auth.verify_token import get_token_header


router = APIRouter(
    prefix="/user-objects",
    tags=["user-objects"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get('/get/{owner_id}', status_code=status.HTTP_302_FOUND)
async def get_user_object(owner_id: str, response: Response) -> dict:
    result = UserObjectActions.get(owner_id)
    
    try:
        if result['status'] == 404:
            response.status_code = result['status']
    except:
        pass
    
    return result


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_objects() -> list:
    return await UserObjectActions.list()


@router.put('/{owner_id}')
async def update_object(owner_id: str, update: dict, response: Response) -> dict:
    result = UserObjectActions.update(owner_id, update)
    
    try:
        if result['status'] == 404:
            response.status_code = result['status']
    except:
        pass
    
    return result


@router.post('/upload')
async def upload(file: UploadFile = File(...)) -> bool:
    
    result = await UserObjectActions.upload(file)
    return result
     


@router.delete('/{owner_id}')
async def delete_object(owner_id: str, response: Response) -> dict:
    result = UserObjectActions.delete(owner_id)
    
    try:
        if result['status'] == 404:
            response.status_code = result['status']
            
    except:
        pass
    
    return result



async def convertToBinaryData(filename):
    # Convert digital data to binary format
    # with open(filename, 'rb') as file:
    #     binaryData = file.read()
    binaryData = await filename.read()
    return binaryData