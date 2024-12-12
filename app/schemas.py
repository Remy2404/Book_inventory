# schemas.py
from pydantic import BaseModel
from typing import Optional

class AuthorBase(BaseModel):
    name: str
    biography: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str
    author_id: int
    category_id: int
    available: Optional[bool] = True

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int
    author: Optional[Author] = None
    category: Optional[Category] = None

    class Config:
        from_attributes = True