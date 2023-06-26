from fastapi import HTTPException
from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from models.model import UserModel

import json


class UserActions:
    
    collection = "Users"
    
    @staticmethod
    def get(uid) -> dict:

        document = db[UserActions.collection].find({"_id": uid})
        
        json_document = UserActions.custom_jsonify(document)
        
        if json_document == []:
            raise HTTPException(status_code=404, detail="User not found")
        
        return json_document[0]


    @staticmethod
    async def list() -> list:

        cursor = db[UserActions.collection].find()
        return UserActions.custom_jsonify( 
                                [document for document in cursor] 
                            )
    
    
    @staticmethod
    def create(user: UserModel):
        
        email_exists = UserActions.validations(user)
        if email_exists:
            return  {
                'error': {
                    'key': 'email', 
                    'message': 'Email Already Exists'
                }
            }
        
        u = user.__dict__
        if u["type"] == 'free-tier':
            u["data_limit"] = 30.0
        elif u["type"] == 'paid':
            u["data_limit"] = 100.0
        
        # Generate User ID
        u["_id"] = uuid4().hex
        
        # Add user to database
        result = db[UserActions.collection].insert_one(u)
        
        return UserActions.get(result.inserted_id)
    
    
    @staticmethod
    def delete(uid: str) -> dict:
        result = db[UserActions.collection].delete_one({'_id': uid})
        if not result.deleted_count:
            return {
                'error': {
                        'key': '_id',
                        'message': 'User with given id is Not Found'
                    }
            }
        
        
        return  {
            'success': {
                'userDeleted': result.acknowledged
            }
        }
    
    
    @staticmethod
    def validations(user: UserModel) -> bool:
        
        found = UserActions.get_documents_count( db[UserActions.collection].find({"email": user.email}).clone() )
        # print(user.email)
        print("\n\n\n", found, "\n\n\n")
            
        if found:
            return True
        
        return False
    
    
    @staticmethod
    def custom_jsonify(doc):
        return json.loads(json_util.dumps(doc))
    
    
    @staticmethod
    async def get_documents_count(doc) -> int:
        return len(list(doc))