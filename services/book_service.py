from sql import crud
from sqlalchemy.orm import Session


def list_book(db: Session):
    return crud.get_all(db)



def get_book(db: Session, book_id: int):
    return crud.get_by_id(db, book_id)


def create_book(db: Session, data: dict):
    return crud.create_book(db, data)



def update_book(db: Session, book_id: int, update: dict):
    return crud.update(db, book_id, update)


def delete_book(db: Session, book_id: int):
    return crud.delete(db, book_id)