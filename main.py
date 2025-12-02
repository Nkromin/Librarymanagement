from fastapi import FastAPI
from routes.book_route import book_router

app = FastAPI(title = "Simple book management api using FastAPI & pandas", version = "1.0.0")

app.include_router(book_router)

@app.get("/")
def home():
    return {"message": "Welcome to the book Management API use/docs"}




