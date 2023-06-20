from pydantic import BaseModel
from .fields import UserFields

class UserModel(BaseModel):
    name: str = UserFields.name
    email: str = UserFields.email
    password: str = UserFields.password
    type: str = UserFields.type
    # data_limit: float = UserFields.data_limit