from fastapi import APIRouter, Depends, HTTPException
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

@router.get('/get/{uid}')
async def get_user(uid: str):
    return UserActions.get(uid)


@router.get('/all')
async def get_all_users():
    return await UserActions.list()
    

@router.post('/register')
async def create_user(create: UserModel):
    uid = uuid4().hex
    user = UserActions.create(create)
    return user


@router.delete('/{uid}')
async def delete_user(uid: str):
    return UserActions.delete(uid)