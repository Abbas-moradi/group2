from fastapi import FastAPI
from routs.user import user_router
from routs.book import book_router


app = FastAPI()
app.include_router(user_router)
app.include_router(book_router)

