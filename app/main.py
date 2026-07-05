from typing import Optional

from fastapi import FastAPI
from sqlmodel import Field, SQLModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World123"}
