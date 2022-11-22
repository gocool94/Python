# FAST API

### Virutal Environment

    -   pip is the packet manager  - Python package manager

### Creating a Virtual environment

      `pip list`

      - Install virtual environment
        `pip install virtualenv`

      - Creating a Virutal environment
        - Syntax : python -m venv EnvironmentName
      
      - Activating the environment
        - EnvironmentName/Scripts/activate

### Installing FAST API

    - Inside the FastAPI folder
      - `pip install fastapi[all]`

### books.py

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    return {"message":"Hello World"}
```

### OPEN API SCHEMA

    - FASTAPI generated Open API Schema so that we can view 
                - http://127.0.0.1:8000/openapi.json
    - FASTAPI comes with **SwaggerUI**
                - http://127.0.0.1:8000/docs

### Project 1

```
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

```

### To run

    uvicorn books:app --reload

## Project 2 - using pydantic

#### books2.py


## SQLAlchemy

Created a Todo application in this.

-> sqlite3 dbname
-> .mode table



## JWT Tokens

jason web token is used to transmit data and information between two parties

JSON WEB TOKEN STRUCTURE:
 header.payload.signature
 aaaaaaa.bbbbbbb.cccccc

JWT Header
    -algorithm
    -the specific type of token

JWT payload
    contains the data 
        - Registered
        - Public
        - Private

JWT Signature
    created using the algorithm in the header to hashout the encoded header

One to Many Relationship


Authentication:


passsword hashing:
    pip install passlib[bcrypt]

    pip install "python-jose[cryptography]"

    pip install psycopg2-binary


Postman

project:

    pip install aiofiles
    pip install jinja2



    
