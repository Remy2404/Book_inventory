# app/models.py
from sqlalchemy import Column, Integer, String, Boolean
from db.connection import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    category = Column(String, index=True)
    available = Column(Boolean, default=True)