from uuid import uuid4
from fastapi import status

from actions.UserActions import UserActions
from helpers.responses import UserResponse
from models.model import UserModel

def test_create_user():
    user_id = uuid4().hex
    
    create = {
        "name": "test python user",
        "email": "test_py@aloha.com",
        "password": "test123",
        "type": "free-tier"
    }
    
    '''Converting dict to UserModel instance'''
    user = UserModel(**create)
    result = UserActions.create(user, user_id)
    
    assert result == UserResponse.CREATED