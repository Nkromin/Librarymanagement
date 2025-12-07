from sqlalchemy.orm import Session
from .models import Book


def get_all(db: Session):
    return db.query(Book).all()

def get_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: dict):
    new_book = Book(**book)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update(db: Session, book_id: int, data: dict):
    existing = get_by_id(db, book_id)
    if not existing:
        return None

    # apply only keys provided in the incoming data dict
    for key, value in data.items():
        # avoid setting attributes that don't exist on the model
        if hasattr(existing, key):
            setattr(existing, key, value)

    db.commit()
    db.refresh(existing)
    return existing

def delete(db: Session, book_id: int):
    book = get_by_id(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book