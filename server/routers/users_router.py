from fastapi import APIRouter, Depends, Response, status
from django.http import JsonResponse
from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from actions.UserActions import UserActions
from actions.UserObjectActions import UserObjectActions
from helpers.responses import UserResponse
from models.model import UserModel

from auth.verify_token import get_token_header
# import json

import re

def email_validation(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
    if(re.fullmatch(regex, email)):
        return True

    return False

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

'''
Starting of all routes with prefix "/users"

'''

@router.get('/get/{arg}', status_code=status.HTTP_302_FOUND)
async def get_user(arg: str, response: Response) -> dict:
    is_arg_email = email_validation(arg)
    if is_arg_email:
        return UserActions.get(email=arg)
    else:
        return UserActions.get(id=arg)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_users() -> list:
    return await UserActions.list()
    
    
@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(create: UserModel, response: Response) -> dict:
    uid = uuid4().hex
    result, created_user = UserActions.create(create, uid)
    
    if result['status'] == status.HTTP_201_CREATED:
        uobj = UserObjectActions.user_object_template(uid, created_user['name'], created_user['data_limit'])
        uobj_result = UserObjectActions.create(uobj)
    
    response.status_code = result['status']
    return result


@router.post('/login', status_code=status.HTTP_302_FOUND)
async def login(cred: dict, response: Response) -> dict:
    result = UserActions.login_user(cred)
    user_id = {}
        
    try:
        response.status_code = result['status']
    except:
        pass
    
    if result != UserResponse.USER_NOT_FOUND('email'):
        user_id['_id'] = result['_id']
        return user_id
    
    return result

@router.delete('/{uid}', status_code=status.HTTP_200_OK)
async def delete_user(uid: str, response: Response) -> dict:
    result = UserActions.delete(uid)
    response.status_code = result['status']
    
    return result
