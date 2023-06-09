from pydantic import BaseModel
from uuid import uuid4
from datetime import date


class Book(BaseModel):
    _id = str[uuid4]
    book_name: str
    author: str
    title: str
    publication_year: date
    genre: str
    availability_status: bool = True
