from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [
    {'title':'title one','author':'Author 1','Category':'Science'},
    {'title':'title two','author':'Author 1','Category':'Social'},
    {'title':'title three','author':'Author three','Category':'History'},
    {'title':'title four','author':'Author four','Category':'Maths'},
    {'title':'title five','author':'Author two','Category':'Maths'}
    ]

@app.get("/books")
async def Read_all_Books():
    return BOOKS


@app.get("/books/Read_book_by_author")
async def read_book_by_author(bookauthor:str):
    books_to_be_returned = []
    for book in BOOKS:
        if book.get('author').casefold() == bookauthor.casefold():
            books_to_be_returned.append(book)
    return books_to_be_returned

@app.get("/books/{book_title}")
async def read_book_by_title(booktitle:str):
    for book in BOOKS:
        if book.get('title').casefold() == booktitle.casefold():
            return {'author':book.get('author'),'Category':book.get('Category')}




@app.get("/books/")
async def categories_of_the_Books(booktitle:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('title').casefold() == booktitle.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/createbook")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/updatebook")
async def updatebook(updated_book= Body()):
    for i in len(BOOKS):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_books/{book_title}")
async def delete_book(book_title:str):
    for i in range(0 ,len(BOOKS)-1):
        print(BOOKS[i])
        if BOOKS[i].get('title') == book_title:
           BOOKS.pop(i)
           break











