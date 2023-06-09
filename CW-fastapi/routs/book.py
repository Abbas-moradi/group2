from utilse.utilse import hash_password, email_validation, encode_access_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from crud.book import return_book_id
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from typing import List, Any, Annotated
from models.book import Book
from storeage import storage
from uuid import uuid4
from pprint import pprint


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
book_router = APIRouter(prefix="/books", tags=["Book"])


@book_router.get("/")
def get_all_book():
    repository = []
    for book in storage.collection_book.find({}, {'_id': 0, 'title': 1, 'author': 1, 'availability_status': 1}):
        repository.append(book)
    return repository


@book_router.get("/genres")
def get_genres_book():
    repository = []
    for genre in storage.collection_book.aggregate([{'$group': {'_id': '$genre', 'total': {'$sum': 1}}}]):
        repository.append(genre)
    return repository


@book_router.get("/search")
def get_book_by_data(word: str):
    repository = []
    for book in storage.collection_book.find({'$or': [{'title': word}, {'author': word}, {'genre': word}]}):
        book['_id'] = str(book['_id'])
        repository.append(book)
    return repository


@book_router.get("/{book_id}")
def get_book_by_id():
    pass


@book_router.post("/")
def add_new_book(book: Book):
    book.publication_year = datetime.strftime(book.publication_year, '%Y %m %d')
    create_book = dict(book)
    book_id = str(uuid4())
    create_book.update({"book_id": book_id})
    storage.collection_book.insert_one(create_book)
    book_id = return_book_id(book_id)
    return {book_id: "book inserted successfully."}


@book_router.put("/")
def update_book():
    pass


@book_router.delete("/")
def delete_book():
    pass
