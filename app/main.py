from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
BOOKS = [
    Book(1, "The Silent Forest", "A. Rahman", "A mysterious tale of a forest where no sound exists.", 4,2010),
    Book(2, "Digital Dreams", "S. Khan", "Exploring a future where AI controls human imagination.", 5,2011),
    Book(3, "Broken Time", "L. Ahmed", "A man discovers he can relive moments from his past.", 3,2012),
    Book(4, "Shadows of Truth", "M. Ali", "A detective uncovers secrets hidden in plain sight.", 4,2013),
    Book(5, "The Last Horizon", "Z. Malik", "A journey to the edge of the universe and beyond.", 5,2010),
    Book(6, "Whispers in the Dark", "H. Siddiqui", "Strange voices lead a girl into a hidden world.", 4,2011),
    Book(7, "Code of Destiny", "F. Hussain", "A programmer finds a code that can change reality.", 5, 2012),
    Book(8, "Echoes of War", "T. Javed", "Stories of soldiers and the aftermath of battle.", 3,2013),
    Book(9, "The Forgotten City", "R. Iqbal", "An ancient city resurfaces with dangerous secrets.", 4,2014),
    Book(10, "Mind Maze", "N. Farooq", "A psychological thriller about escaping one's own mind.", 5,2015)
]


class BookRequest(BaseModel):
    id: Optional[int] =  Field(description="No id needed on create", default=None)
    title: str = Field(min_length=3, max_length=20)
    author: str = Field(min_length=3, max_length=15)
    description: str = Field(min_length=3, max_length= 50)
    rating: int = Field(gt=0,lt=6)
    published_date: int = Field(gt=1900, lt= 2100)

    model_config= {
        "json_schema_extra":{
            "example":{
                "title":"A new Book",
                "author":"Coding With Roby",
                "description":"Best book for coding",
                "rating":5,
                "published_date":2020
            }
        }
    }
    


@app.get("/")
async def root():
    return {"message":"This app is working"}


@app.get("/books/{book_id}")
async def find_book_by_id(book_id:int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def books_by_rating(book_rating : int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book")
async def update_a_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
    return BOOKS

@app.delete("/books/{book_id}")
async def delete_a_book(book_id:int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


@app.get("/books/books_by_date/")
async def books_by_date(publish_date : int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == publish_date:
            books_to_return.append(book)
    return books_to_return

@app.get("/books")
async def all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))








def find_book_id(book: Book):


    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1] + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1

    # else:
    #     book.id = 1
    
    return book
