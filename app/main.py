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


@app.get("/books/public/{book_id}")
async def get_public_book(book_id: int):
    return {"message": f"public book with id {book_id} endpoint"}


@app.post("/books/public")
async def create_public_book():
    return {"message": "create public book endpoint"}


@app.patch("/books/public/{book_id}")
async def update_public_book(book_id: int):
    return {"message": f"update public book with id {book_id} endpoint"}


@app.delete("/books/public/{book_id}")
async def delete_public_book(book_id: int):
    return {"message": f"delete public book with id {book_id} endpoint"}


@app.get("/authors")
async def get_authors():
    return {"message": "all authors endpoint"}


@app.get("/authors/{author_id}")
async def get_author(author_id: int):
    return {"message": f"author with id {author_id} endpoint"}


@app.post("/authors")
async def create_author():
    return {"message": "create author endpoint"}


@app.patch("/authors/{author_id}")
async def update_author(author_id: int):
    return {"message": f"update author with id {author_id} endpoint"}


@app.delete("/authors/{author_id}")
async def delete_author(author_id: int):
    return {"message": f"delete author with id {author_id} endpoint"}


@app.get("/genres")
async def get_genres():
    return {"message": "all genres endpoint"}


@app.get("/genres/{genre_id}")
async def get_genre(genre_id: int):
    return {"message": f"genre with id {genre_id} endpoint"}


@app.post("/genres")
async def create_genre():
    return {"message": "create genre endpoint"}


@app.patch("/genres/{genre_id}")
async def update_genre(genre_id: int):
    return {"message": f"update genre with id {genre_id} endpoint"}


@app.delete("/genres/{genre_id}")
async def delete_genre(genre_id: int):
    return {"message": f"delete genre with id {genre_id} endpoint"}