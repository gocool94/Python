from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1':{'title':'TitleOne','author':'AuthorOne'},
    'book_2':{'title':'TitleTwo','author':'AuthorTwo'},
    'book_3':{'title':'TitleThree','author':'AuthorThree'},
    'book_4':{'title':'TitleFour','author':'AuthorFour'},
    'book_5':{'title':'TitleFive','author':'AuthorFive'},

}

class Direction(str, Enum):
    north = "north"
    south = "south"
    east = "east"
    west = "west"

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/{bookname}")
async def read_book_provided(bookname:str):
    return BOOKS[bookname]

@app.get("/books/{book_title}")
async def read_book(book_title):
    return {"Books":book_title}

@app.get("/books/{book_id}")
async def read_book_byid(book_id:int):
    return {"Books":book_id}


#qwery parameter
@app.get("/readallbooks")
async def readallbooks(skip_book:str = "Book3"):
    new_book = BOOKS.copy()
    del new_book[skip_book]
    return new_book

#post request
@app.post("/")
async def create_book(book_title,book_author):
    current_book_id = 0

    if len(BOOKS)>0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            print(x)
            if x > current_book_id:
                current_book_id = x
    BOOKS[f"book_{current_book_id+1}"]={"title":book_title,"author":book_author}

    return BOOKS[f"book_{current_book_id+1}"]

#put request
@app.put("/{book_name}")
async def update_book(Bookname:str,BookTitle:str,BookAuthor:str):
    bookInformation = {"title":BookTitle,"author":BookAuthor}
    BOOKS[Bookname] = bookInformation
    return bookInformation

#delete request
@app.delete('/{book_name}')
async def delete_books(bookname:str):
    del BOOKS[bookname]
    return f'{bookname} Deleted' 




#using enum and a class
@app.get("/directions/{direction_name}")
async def get_direction(direction_name:Direction):
    if direction_name == Direction.north:
        return {"direction":direction_name,"sub":"up"}
    if direction_name == Direction.south:
        return {"direction":direction_name,"sub":"down"}
    if direction_name == Direction.east:
        return {"direction":direction_name,"sub":"left"} 
    return {"direction":direction_name,"sub":"right"}

