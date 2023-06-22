from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from models.model import UserModel

import json

class UserActions:
    
    collection = "Users"
    
    @staticmethod    
    def get(uid):

        document = db[UserActions.collection].find({"_id": uid})
        if not document:
            return {'message': 'User not found'}
        
        return json.loads(json_util.dumps( document ))
    
    
    @staticmethod
    def list():

        cursor = db[UserActions.collection].find()
        return json.loads(json_util.dumps(
                                [document for document in cursor]
                            ))
    
    
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
            u["`data_limit`"] = 30.0
        
        u["_id"] = uuid4().hex
        result = db[UserActions.collection].insert_one(u)
        
        return UserActions.get(result.inserted_id)
    
    
    @staticmethod
    def delete(uid: str):
        result = db[UserActions.collection].delete_one({'_id': uid})
        if not result.deleted_count:
            return {
                'error': {   
                        'key': '_id', 
                        'message': 'User with _id Not Found'
                    }
            }
        return  {
                    'success': {
                            'userDeleted': result.acknowledged
                        }
                }
    
    
    @staticmethod
    def validations(user: UserModel):
        
        found = len(list( db[UserActions.collection].find({"email": user.email}).clone() ))
        # print(user.email)
        print("\n\n\n", found, "\n\n\n")
            
        if found:
            return True
        