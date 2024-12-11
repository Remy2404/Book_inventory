# app/routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import services, schemas
from db.connection import SessionLocal

router = APIRouter(
    prefix="/books",
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
    return services.create_book(db, book)

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