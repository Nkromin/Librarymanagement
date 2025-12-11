from sql import crud
from sql.crud import get_by_anime_id
from sqlalchemy.orm import Session


def list_anime(db: Session):
    return crud.get_all_anime(db)


def get_anime(db: Session, anime_id: int):
    return crud.get_by_anime_id(db, anime_id)


def create_anime(db: Session, data: dict):
    return crud.create_anime(db, data)


def update_anime(db: Session, anime_id: int, update: dict):
    return crud.update_anime(db, anime_id, update)


def delete_anime(db: Session, anime_id: int):
    anime = get_by_anime_id(db, anime_id)
    if not anime:
        raise Exception("Anime not found")
    else:
        try:
            if anime.genre == "X":
                deleted_anime = crud.delete_anime(db, anime_id)
                deleted_book = crud.delete_book(db, anime.book_id)
            else:
                deleted_anime = crud.delete_anime(db, anime_id)
        except Exception as e:
            raise Exception(f"Error deleting associated book: {str(e)}")
    return deleted_anime