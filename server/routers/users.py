from fastapi import APIRouter, Depends, HTTPException
from django.http import JsonResponse
from bson import json_util
from helpers.db_config import db

from models.model import UserModel

from auth.verify_token import get_token_header
import json

router = APIRouter(
    prefix="/db",
    tags=["db"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

'''
Starting of all routes starting with prefix "/db"

'''

@router.get('/list')
async def _list_collections():

    return { "db": db.list_collection_names() }

@router.get('/all/{collection}')
async def _get_all_users_in_collection(collection: str):
    
    cursor = db[collection].find()
    
    users_list = []
    for document in cursor:
          users_list.append(document)
    
    if users_list:
        return { "Users": json.loads(json_util.dumps(users_list)) }
    else:
        return { "Users": "Collection is empty!"}

@router.post('/register')
async def _create_user(create: UserModel):
    if create['type'] == 'free-tier':
        create['data_limit'] = 30.0
    return create