from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field
from typing import Annotated


class Author(BaseModel):
    id: int
    name: str
    bio: str


class Genre(BaseModel):
    id: int
    name: str
    description: str


class Book(BaseModel):
    id: int
    title: str
    description: str
    year: int
    author_id: int
    genre_id: int


class FilterParams(BaseModel):
    offset: int = Field(0, ge=0, le=5000)
    limit: int = Field(10, ge=1, le=100)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "root endpoint"}

@app.get("/books/public")
async def get_public_books(filter_params: Annotated[FilterParams, Query()]):
    return {"message": f"all public books endpoint. offset: {filter_params.offset}, limit: {filter_params.limit}"}


@app.get("/books/public/{book_id}")
async def get_public_book(book_id: Annotated[int, Path(ge=1)]):
    return {"message": f"public book with id {book_id} endpoint"}


@app.post("/books/public")
async def create_public_book():
    return {"message": "create public book endpoint"}


@app.patch("/books/public/{book_id}")
async def update_public_book(book_id: Annotated[int, Path(ge=1)]):
    return {"message": f"update public book with id {book_id} endpoint"}


@app.delete("/books/public/{book_id}")
async def delete_public_book(book_id: Annotated[int, Path(ge=1)]):
    return {"message": f"delete public book with id {book_id} endpoint"}

@app.get("/authors")
async def get_authors(filter_params: Annotated[FilterParams, Query()]):
    return {"message": f"all authors endpoint. offset: {filter_params.offset}, limit: {filter_params.limit}"}


@app.get("/authors/{author_id}")
async def get_author(author_id: Annotated[int, Path(ge=1)]):
    return {"message": f"author with id {author_id} endpoint"}


@app.post("/authors")
async def create_author():
    return {"message": "create author endpoint"}


@app.patch("/authors/{author_id}")
async def update_author(author_id: Annotated[int, Path(ge=1)]):
    return {"message": f"update author with id {author_id} endpoint"}


@app.delete("/authors/{author_id}")
async def delete_author(author_id: Annotated[int, Path(ge=1)]):
    return {"message": f"delete author with id {author_id} endpoint"}

@app.get("/genres")
async def get_genres(filter_params: Annotated[FilterParams, Query()]):
    return {"message": f"all genres endpoint. offset: {filter_params.offset}, limit: {filter_params.limit}"}


@app.get("/genres/{genre_id}")
async def get_genre(genre_id: Annotated[int, Path(ge=1)]):
    return {"message": f"genre with id {genre_id} endpoint"}


@app.post("/genres")
async def create_genre():
    return {"message": "create genre endpoint"}


@app.patch("/genres/{genre_id}")
async def update_genre(genre_id: Annotated[int, Path(ge=1)]):
    return {"message": f"update genre with id {genre_id} endpoint"}


@app.delete("/genres/{genre_id}")
async def delete_genre(genre_id: Annotated[int, Path(ge=1)]):
    return {"message": f"delete genre with id {genre_id} endpoint"}
