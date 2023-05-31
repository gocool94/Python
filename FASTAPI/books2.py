from fastapi import FastAPI, Body , Path , Query , HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status



app = FastAPI()



class Book:
    id : int
    title : str
    author : str
    description : str
    rating : int
    published_date : int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title= title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field("Id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=2 , max_length= 100)
    description: str = Field(min_length=1)
    rating: int = Field(gt=0,lt=6)
    published_date :int = Field(gt = 1999, lt= 2023)

    class Config:
        schema_extra = {
            'example': {
                'title': 'A new book',
                    'author':'Some author',
                        'description':'Description of the book',
                            'rating':'2',
                                'published_date':'2016',
            }
        }




BOOKS = [

Book(1,"Economics for life","Anand","Good Book",5,2016),
Book(2,"Science for life","einstein","Good kkkkk",4,2015),
Book(3,"Social for life","rudra","Good mmmmmmmm",3,2012),
Book(4,"Maths for life","zroo","Good jjjjjjj",4,2022),
Book(5,"english for life","Williomson","Good Boiiiiiiiok",3,2021),
Book(6,"MBBS for life","cherian","Good oiiiiiiii",5,2000)

]

@app.get("/Books",status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/Books/{book_id}",status_code=status.HTTP_200_OK)
async def read_book_with_id(book_id : int = Path(gt=0)) :
    for book in BOOKS:
        if book_id == book.id:
            return book
    raise HTTPException(status_code=404,detail="Item not found")

@app.get("/Books/",status_code=status.HTTP_200_OK)
async def read_books_with_rating(book_rating: int = Query(gt=0,lt=6)):
    books_of_rating = []
    for book in BOOKS:
        if book_rating == book.rating:
            books_of_rating.append(book)
    return books_of_rating

@app.get("/Books/published/",status_code=status.HTTP_200_OK)
async def fetch_published_date(published_date : int= Query(gt=1999,lt=2023)):
    Books_selected = []
    for book in BOOKS:
        print(book.published_date)
        if published_date == book.published_date:
            Books_selected.append(book)
    return Books_selected



@app.post("/createBook",status_code=status.HTTP_201_CREATED)
async def create_books(book_request: BookRequest):
    print(BookRequest)
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

@app.put("/books/updatebook",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest ):
    book_status = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id  == book.id:
            BOOKS[i] = book
            book_status = True
    if not book_status :
        raise HTTPException(status_code=404,detail="Item not found")




@app.delete("/Books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_with_id(book_id : int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        print(i)
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if  not book_changed:
        raise HTTPException(status_code=404,detail="Item not found")





def find_book_id(book : Book):
    if (len(BOOKS) > 0):
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    print(book.id)
    print(book.title)
    return book