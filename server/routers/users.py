from fastapi import APIRouter, Depends, Response, status
from django.http import JsonResponse
from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from actions.UserActions import UserActions
from actions.UserObjectActions import UserObjectActions
from models.model import UserModel

from auth.verify_token import get_token_header
# import json

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

'''
Starting of all routes with prefix "/users"

'''

@router.get('/get/{uid}', status_code=status.HTTP_302_FOUND)
async def get_user(uid: str, response: Response) -> dict:
    return UserActions.get(uid)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_users() -> list:
    return await UserActions.list()
    

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(create: UserModel, response: Response) -> dict:
    uid = uuid4().hex
    result = UserActions.create(create, uid)
    
    response.status_code = result['status']
    return result


@router.delete('/{uid}', status_code=status.HTTP_200_OK)
async def delete_user(uid: str, response: Response) -> dict:
    result = UserActions.delete(uid)
    response.status_code = result['status']
    
    return result
