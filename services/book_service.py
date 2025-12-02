import pandas as pd

from sql import CRUD


def list_book():
    df = CRUD.load_data()

    return df.to_dict(orient="records")


def get_book(book_id):
    df = CRUD.load_data()
    book = df[df["id"] == book_id]

    if book.empty:
        return None

    return book.to_dict(orient="records")


def create_book(data: dict):
    df = CRUD.load_data()
    new_id = CRUD.next_id(df)

    new_row = {"id": new_id, "title": data['title'], "author": data['title'], "genre": data['genre'],
               "year": data['year'], "available": data.get('available', True), }

    df = pd.concat([df,pd.DataFrame([new_row])], ignore_index=True)
    CRUD.save_data(df)

    return new_row


def update_book(book_id: int, update: dict):
    df = CRUD.load_data()

    if book_id not in df["id"].values:
        return None

    for key, value in update.items():
        df.loc[df["id"] == book_id, key] = value

    CRUD.save_data(df)

    return df[df["id"] == book_id].iloc[0].to_dict()


def delete_book(book_id: int):
    df = CRUD.load_data()

    if book_id not in df["id"].values:
        return False

    df = df[df["id"] != book_id]

    CRUD.save_data(df)

    return True