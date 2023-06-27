from typing import Optional
from pydantic import BaseModel
from .fields import UserFields

class UserModel(BaseModel):
    _id: Optional[str] = UserFields._id
    name: str = UserFields.name
    email: str = UserFields.email
    password: str = UserFields.password
    type: str = UserFields.type
    # data_limit: float = UserFields.data_limit

    
class UserObjectsModel(BaseModel):
    uid: Optional[str]
    name: str
    objects: list
    free_space_remaining: float
    total_objects: int
    