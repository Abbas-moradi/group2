from storeage.storage import collection_user
from fastapi import HTTPException, status
from utilse.utilse import verify_password
from typing import Any


def user_name_exists(username: str):
    if list(collection_user.find({"username": username})):
        return True
    return False


def return_user_id(username: str) -> id:
    return_user = list(collection_user.find({"username": username}))
    return_id = return_user[0]["_id"]
    return return_id


def return_user_password(username: str) -> str:
    return_user_hash_password = list(collection_user.find({"username": username}))
    return_user_hash_password = return_user_hash_password[0]["password"]
    return return_user_hash_password


def authenticate_user(username, password):
    user = user_name_exists(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username doesn't exist")
    if verify_password(password, return_user_password(username)):
        return {"username": username, "password": password}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")


def return_user_role(username):
    role_user = list(collection_user.find({"username": username}))
    role_user = role_user[0]["role"]
    return role_user
