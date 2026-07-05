from typing import Optional

from fastapi import FastAPI
from sqlmodel import Field, SQLModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "root endpoint"}


@app.get("/books/public")
async def get_public_books():
    return {"message": "all public books endpoint"}


@app.get("/books/public/{book_id}"):
async def get_public_book(book_id: int):
    return {"message": f"public book with id {book_id} endpoint"}


@app.post("/books/public")
async def create_public_book():
    return {"message": "create public book endpoint"}


@app.patch("/books/public/{book_id}"):
async def update_public_book(book_id: int):
    return {"message": f"update public book with id {book_id} endpoint"}


@app.delete("/books/public/{book_id}"):
async def delete_public_book(book_id: int):
    return {"message": f"delete public book with id {book_id} endpoint"}