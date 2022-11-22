from fastapi import FastAPI , HTTPException,Request,status,Form,Header
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

from starlette.responses import JSONResponse



class NegativeNumberException(Exception):
    def __init__(self,books_to_return):
        self.book_to_return = books_to_return

app = FastAPI()

BOOKS = []

class Book(BaseModel):
    id:UUID
    title:str = Field(min_length=5)
    author:str = Field(min_length=4,max_length=75)
    description:str = Field(title="Description of the book",max_length=100,min_length=2)
    rating:int = Field(gt=-1,lt=10)
    class Config:
        schema_extra = {
            "example":{
                "id":"21f4c2ea-1340-41f4-89f7-2852347bb0d1",
                "title":"This is the title",
                "author":"Author",
                "description":"description",
                "rating":6
            }
        }

class BookNoRating(BaseModel):
    id:UUID
    title: str = Field(min_length=1)
    author:str
    description:Optional[str] = Field(
        None,title="description of the book",
        max_length=100,
        min_length = 2
    )


@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request:Request,exception:NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={"message":f"hey why do you want {exception.book_to_return}"}
    )


@app.get("/books/rating/{book_id}",response_model=BookNoRating)
async def get_bookid_without_rating(book_id:UUID):
    for  x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_exception_cannot_be_found()

@app.post("/books/login/")
async def login_to_books(book_id : int, username: Optional[str] = Header(), password: Optional[str]=Header()):
    if(username=="gokul" and password=="123"):
        return BOOKS[0]
    return "Invalid user"





@app.get('/header')
async def get_header(random_header:Optional[str] = Header(None)):
    return {'random_header':random_header}

@app.get("/books/{book_id}")
async def get_bookid(book_id:UUID):
    for  x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_exception_cannot_be_found()

@app.get("/")
async def read_all_books(books_to_be_viewed: Optional[int] = None):

    if(books_to_be_viewed and books_to_be_viewed<0):
        raise NegativeNumberException(books_to_return=books_to_be_viewed)

    if len(BOOKS) < 1:
        create_books_api()

    if books_to_be_viewed and len(BOOKS) >= books_to_be_viewed > 0:
        i = 1
        new_books = []
        while i <= books_to_be_viewed:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books

    return BOOKS

@app.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book:Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
async def update_book(book_id:UUID,book:Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter-1] = book
            return BOOKS[counter-1]
    raise raise_exception_cannot_be_found()


@app.delete('/{book_id}')
async def delete_book(book_id:UUID):
    counter = 0
    for each_book in BOOKS:
        counter+=1
        if each_book.id == book_id:
            del BOOKS[counter-1]
            return f"successfully deleted {book_id}"
    raise raise_exception_cannot_be_found()





def create_books_api():
    book_1 = Book(id="71f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=6)
    book_2 = Book(id="21f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=7)
    book_3 = Book(id="31f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=8)
    book_4 = Book(id="41f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=9)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)


def raise_exception_cannot_be_found():
    return HTTPException(status_code=404, detail="Books not found", headers={"X-Header-Error":
                                                                                "Nothing to be seen at the UUID"})



