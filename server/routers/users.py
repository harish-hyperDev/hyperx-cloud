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

@router.get('/get/{uid}')
async def get_user(uid: str):
    return UserActions.get(uid)


@router.get('/all')
async def get_all_users():
    return UserActions.list()
    

@router.post('/register')
async def create_user(create: UserModel):
    return UserActions.create(create)


@router.delete('/{uid}')
async def delete_user(uid: str):
    return UserActions.delete(uid)
    pass