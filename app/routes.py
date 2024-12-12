# routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import services, schemas
from typing import List
from db.connection import SessionLocal

router = APIRouter(
    prefix="",
    tags=["books"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db=db, book=book)

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = services.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.get("/", response_model=list[schemas.Book])
def read_books(
    skip: int = 0,
    limit: int = 10,
    title: str = Query(None, description="Filter by book title"),
    author: str = Query(None, description="Filter by author name"),
    category: str = Query(None, description="Filter by category"),
    available: bool = Query(None, description="Filter by availability"),
    db: Session = Depends(get_db)
):
    books = services.get_books(db, skip=skip, limit=limit, title=title, author=author, category=category, available=available)
    return books

@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = services.update_book(db, book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = services.delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
@router.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return services.create_author(db=db, author=author)

@router.get("/authors/{author_id}", response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    return services.get_author(db=db, author_id=author_id)

@router.get("/authors/", response_model=List[schemas.Author])
def list_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.list_authors(db=db, skip=skip, limit=limit)

@router.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return services.update_author(db=db, author_id=author_id, author=author)

@router.delete("/authors/{author_id}", response_model=schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    return services.delete_author(db=db, author_id=author_id)

# Category Routes
@router.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return services.create_category(db=db, category=category)

@router.get("/categories/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return services.get_category(db=db, category_id=category_id)

@router.get("/categories/", response_model=List[schemas.Category])
def list_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.list_categories(db=db, skip=skip, limit=limit)

@router.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return services.update_category(db=db, category_id=category_id, category=category)

@router.delete("/categories/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return services.delete_category(db=db, category_id=category_id)