from utilse.utilse import hash_password, email_validation, encode_access_token, decode_access_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from crud.user import user_name_exists, return_user_id, authenticate_user, return_user_role
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from typing import List, Any, Annotated
from models.user import User, UserUpdate
from models.session import Session
from storeage import storage
from jose import jwt, JWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
user_router = APIRouter(prefix="/users", tags=["User"])


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        data = decode_access_token(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return data


@user_router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    user_role = return_user_role(user["username"])
    access_token = encode_access_token(data={"sub": user["username"], "role": user_role})
    session = Session(username=user["username"])
    storage.Session[session.session_id] = session
    login_time = datetime.now()
    response = JSONResponse(
        content={
            "message": "Login successful",
            "access_token": access_token,
            "token_type": "bearer"
        }
    )
    expires = login_time + timedelta(minutes=30)
    response.set_cookie(key='session_id', value=session.session_id,
                        expires=datetime.strftime(expires, '%Y %m %d'))
    return response


@user_router.post("/register")
def register(user: User):
    if user_name_exists(user.username):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User has been exists...")
    if email_validation(user.email):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email has been exists")
    user.password = hash_password(user.password)
    user_in = dict(user)
    user_in.update({'role': 'regular'})
    storage.collection_user.insert_one(user_in)
    user_id = return_user_id(user_in["username"])
    return {f"{user_id}": "user created"}
    

@user_router.put("/")
def user_update(username, user: UserUpdate, current_user: str = Depends(get_current_user)):
    if not current_user["role"].lower() == "admin":
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="user is not admin...")
    if not user_name_exists(username):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User has not been exists...")
    if user_name_exists(user.username):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User has been exists...")
    if email_validation(user.email):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email has been exists")
    user.password = hash_password(user.password)
    user_storage_update = dict(user)
    user_id = return_user_id(username)
    storage.collection_user.update_one({"_id": user_id}, {"$set": {**user_storage_update}})
    return {str(user_id): "User has been update..."}


@user_router.delete("/")
def user_delete(username, current_user: str = Depends(get_current_user)):
    if not current_user["role"].lower() == "admin":
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="user is not admin...")
    if not user_name_exists(username):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User has not been exists...")
    if current_user["sub"] == username:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="can not delete your self...")
    user_id = return_user_id(username)
    storage.collection_user.delete_one({"_id": user_id})
    return {str(user_id): "User has been deleted..."}



