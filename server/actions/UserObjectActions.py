from fastapi import HTTPException
from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from models.model import UserObjectModel


class UserObjectActions:
    
    collection = "UserObjects"
    
    @staticmethod
    def create(uobj: UserObjectModel):
        check = UserObjectActions.validations(uobj)
        if check:
            return
        db[UserObjectActions.collection].insert_one(uobj)
    
    @staticmethod
    def create_user_object_template(source_uid: str, source_name: str, source_free_space: float) -> dict:
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
        pass
    