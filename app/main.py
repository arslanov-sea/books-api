from typing import Optional

from fastapi import FastAPI
from sqlmodel import Field, SQLModel

app = FastAPI()


class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    bio: str | None = Field(default=None, max_length=1000)


class Genre(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=50, unique=True)
    description: str | None = Field(default=None, max_length=500)


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=200)
    author_id: int = Field(foreign_key="author.id")
    genre_id: int = Field(foreign_key="genre.id")
    year: int = Field()
    pages: int | None = Field(default=None)
    is_available: bool = Field(default=True)


@app.get("/")
async def root():
    return {"message": "Hello World123"}
