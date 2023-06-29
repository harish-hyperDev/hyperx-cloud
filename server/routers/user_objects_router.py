from fastapi import APIRouter, Depends, Response, status
from django.http import JsonResponse
from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from actions.UserActions import UserActions
from actions.UserObjectActions import UserObjectActions
from models.model import UserModel

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


@router.patch('/{owner_id}')
async def update_object(owner_id: str, update: dict, response: Response) -> dict:
    result = UserObjectActions.update(owner_id, update)
    
    try:
        if result['status'] == 404:
            response.status_code = result['status']
    except:
        pass
    
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