from sql import crud
from sql.models import Book, Anime
from sqlalchemy.orm import Session

def list_anime(db: Session):
    return crud.get_all_anime(db)

def get_anime(db: Session, anime_id: int):
    return crud.get_anime_by_id(db, anime_id)


def create_anime(db: Session, data: dict):
    anime = Anime(**data)
    return crud.create_anime(db, anime)


def update_anime(db: Session, anime_id: int, update: dict):
    return crud.update_anime_by_id(db, anime_id, update)


def delete_anime(db: Session, anime_id: int):
    anime = crud.get_anime_by_id(db, anime_id)

    if not anime:
        return None

    crud.delete_anime(db, anime)
    return True
