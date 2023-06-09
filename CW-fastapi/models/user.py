from pydantic import BaseModel
from uuid import uuid4
from utilse.utilse import hash_password


class User(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(User):
    username: str
    email: str
    password: str
    role: str



