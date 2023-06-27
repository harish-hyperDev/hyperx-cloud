from uuid import uuid4
from fastapi import status

from actions.UserActions import UserActions
from helpers.responses import UserResponse
from models.model import UserModel

def test_create_user():
    user_id = uuid4().hex
    
    create = {
        "name": "test program3",
        "email": "test_program51@aloha.com",
        "password": "test",
        "type": "free-tier"
    }
    
    '''Converting dict to UserModel instance'''
    user = UserModel(**create)
    result = UserActions.create(user, user_id)
    
    assert result == UserResponse.CREATED