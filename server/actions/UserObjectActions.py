from fastapi import HTTPException
from bson import json_util
from uuid import uuid4

from helpers.db_config import db
from models.model import UserModel, UserObjectsModel


class UserObjectActions:
    
    collection = "UserObjects"
    
    def create(uobj: UserObjectsModel):
        pass
    