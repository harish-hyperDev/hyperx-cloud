from fastapi import APIRouter, Depends, HTTPException
from django.http import JsonResponse
from bson import json_util

from helpers.db_config import db
from actions.UserActions import UserActions
from models.model import UserModel

from auth.verify_token import get_token_header
import json

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

'''
Starting of all routes starting with prefix "/db"

'''

@router.get('/')

@router.get('/all')
async def get_all_users():
    return UserActions.list()
    # cursor = db[collection].find()
    
    # users_list = []
    # for document in cursor:
    #       users_list.append(document)
    
    # if users_list:
    #     return { "Users": json.loads(json_util.dumps(users_list)) }
    # else:
    #     return { "Users": "Collection is empty!"}

@router.post('/register')
async def create_user(create: UserModel):
    return UserActions.create(create)