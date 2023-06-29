from bson import json_util

from helpers.db_config import db
from helpers.responses import UserResponse, UserObjectResponse
from models.model import UserObjectModel
from actions.UserActions import UserActions

import json

class UserObjectActions:
    
    collection = "UserObjects"
    
    @staticmethod
    def get(owner_id: str):
        
        object_document = {}
        
        object_document = db[UserObjectActions.collection].find({"owner_id": owner_id})
        
        json_object_document = UserObjectActions.custom_jsonify(object_document)
        
        if json_object_document == []:
            return UserObjectResponse.OBJECT_NOT_FOUND
        
        return json_object_document[0]
    
    
    @staticmethod
    async def list() -> dict:
        users = db[UserObjectActions.collection].find()
        return UserObjectActions.custom_jsonify(
            [user for user in users]
        )
    
    '''
    FUNCTION to create a user object in UserObjects collection
    RETURNS dict
    '''
    @staticmethod
    def create(uobj: UserObjectModel):
        uid_not_found = UserObjectActions.validations(uobj)
        
        if uid_not_found:
            return UserResponse.USER_NOT_FOUND
        
        result = db[UserObjectActions.collection].insert_one(uobj)
    
    '''
    FUNCTION to create a user object
    RETURNS dict
    '''
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
    def delete(owner_id: str):
        result = db[UserObjectActions.collection].delete_one({"owner_id": owner_id})
        
        if not result.deleted_count:
            return UserObjectResponse.OBJECT_NOT_FOUND
    
    @staticmethod
    def validations(validate_obj: UserObjectModel):
        uid = validate_obj['owner_id']
        
        result = UserActions.get(id=uid)
        if result != UserResponse.USER_NOT_FOUND:
            return False
        
        return True
    
    
    @staticmethod
    def custom_jsonify(doc) -> list:
        return json.loads(json_util.dumps(doc))