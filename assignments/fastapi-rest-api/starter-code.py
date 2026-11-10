from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Biblioteca de Livros")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books = [
    Book(id=1, title="O Pequeno Príncipe", author="Antoine de Saint-Exupéry"),
    Book(id=2, title="A Ilha do Tesouro", author="Robert Louis Stevenson"),
]


@app.get("/books", response_model=list[Book])
def list_books():
    pass


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_data: BookCreate):
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    pass
