# app/schemas.py
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    category: str
    available: bool

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True