from fastapi import HTTPException
from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from helpers.responses import UserResponse
from models.model import UserObjectModel
from actions.UserActions import UserActions


class UserObjectActions:
    
    collection = "UserObjects"
    
    @staticmethod
    def get(owner_id: str):
        pass
    
    @staticmethod
    def create(uobj: UserObjectModel):
        uid_not_found = UserObjectActions.validations(uobj)
        
        if uid_not_found:
            return UserResponse.USER_NOT_FOUND
        
        result = db[UserObjectActions.collection].insert_one(uobj)
        
    
    @staticmethod
    def user_object_template(source_uid: str, source_name: str, source_free_space: float) -> dict:
        user_object = {
            "owner_id": source_uid,
            "name": source_name,
            "objects": [],
            "free_space_remaining": source_free_space,
            "total_objects": 0
        }
        
        return user_object
    
    @staticmethod
    def validations(validate_obj: UserObjectModel):
        uid = validate_obj['owner_id']
        
        result = UserActions.get(uid)
        if result != UserResponse.USER_NOT_FOUND:
            return False
        
        return True
    