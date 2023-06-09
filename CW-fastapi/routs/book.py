from utilse.utilse import hash_password, email_validation, encode_access_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from crud.user import user_name_exists, return_user_id, authenticate_user
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from typing import List, Any, Annotated
from models.user import User
from models.session import Session
from storeage import storage


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
book_router = APIRouter(prefix="/books", tags=["Book"])


@book_router.get("/")
def get_all_book():
    pass


@book_router.get("/search")
def get_book_by_data():
    pass


@book_router.get("/{book_id}")
def get_book_by_id():
    pass


@book_router.post("/")
def add_new_book():
    pass


@book_router.post("/genres")
def get_genres_book():
    pass


@book_router.put("/")
def update_book():
    pass


@book_router.delete("/")
def delete_book():
    pass
