from fastapi import HTTPException, status
from bson import json_util

from helpers.db_config import db
from models.model import UserModel
from helpers.responses import UserResponse

import json


class UserActions:
    
    collection = "Users"
    
    @staticmethod
    def get(uid: str) -> dict:

        document = db[UserActions.collection].find({"_id": uid})
        
        json_document = UserActions.custom_jsonify(document)
        
        if json_document == []:
            return UserResponse.USER_NOT_CREATED
        
        return json_document[0]


    @staticmethod
    async def list() -> list:

        cursor = db[UserActions.collection].find()
        return UserActions.custom_jsonify( 
                                [document for document in cursor]
                            )
    
    
    @staticmethod
    def create(user: UserModel, uid: str) -> dict:
        
        email_exists = UserActions.validations(user)
        if email_exists:
            return UserResponse.USER_ALREADY_EXISTS
        
        u = user.__dict__
        if u["type"] == 'free-tier':
            u["data_limit"] = 30.0
        elif u["type"] == 'paid':
            u["data_limit"] = 100.0
        
        # Generate User ID
        u["_id"] = uid
        
        # Add user to database
        result = db[UserActions.collection].insert_one(u)
        
        user = UserActions.get(result.inserted_id)
        
        if user != UserResponse.USER_NOT_CREATED:
            return UserResponse.USER_CREATED, user
        
        return user
    
    @staticmethod
    def delete(uid: str) -> dict:
        result = db[UserActions.collection].delete_one({'_id': uid})
        
        if not result.deleted_count:
            return UserResponse.USER_NOT_FOUND
        
        
        return UserResponse.USER_DELETED
    
    
    @staticmethod
    def validations(user: UserModel) -> bool:
        
        found = len(list( db[UserActions.collection].find({"email": user.email}).clone() ))
            
        if found:
            return True
        
        return False
    
    
    @staticmethod
    def custom_jsonify(doc) -> list:
        return json.loads(json_util.dumps(doc))
    
    
    @staticmethod
    async def get_documents_count(doc) -> int:
        return len(list(doc))