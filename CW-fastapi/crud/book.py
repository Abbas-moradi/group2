from storeage.storage import collection_book
from fastapi import HTTPException,status


def title_exists(title: str) -> bool:
    if collection_book.find({'title': title}):
        return True
    return False


def return_book_id(book_id: str) -> str:
    book_id = list(collection_book.find({'book_id': book_id}))
    if not book_id[0]['book_id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="book not found.")
    return book_id[0]['book_id']
