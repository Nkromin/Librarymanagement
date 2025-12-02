from fastapi import APIRouter
from services.book_service import list_book, get_book, create_book, update_book, delete_book

book_router = APIRouter(prefix="/book", tags=["books"])

@book_router.get("/", summary="List all books")
def list_all():
    return list_book()

@book_router.get("/{book_id}",)
def single_book(book_id: int):
    book = get_book(book_id)
    if book:
        return book
    else:
        return {"error": "Book not found"}

@book_router.post("/", summary="Create a new book")
def add_book(data: dict):
    return create_book(data)

@book_router.put("/{book_id}", summary="Update a book")
def modify_book(book_id: int, data: dict):
    updated_book = update_book(book_id, data)
    if updated_book:
        return updated_book
    else:
        return{"error": "Book not found"}


@book_router.delete("/{book_id}", summary="Delete a book")
def remove_book(book_id: int):
    deleted = delete_book(book_id)
    if deleted:
        return {"message": "Book deleted successfully"}
    else:
        return {"error": "Book not found"}




