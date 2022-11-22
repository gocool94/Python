"""
from fastapi import FastAPI, Depends,HTTPException, Request
import models
from typing import Optional
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from pydantic import BaseModel,Field
from starlette.responses import JSONResponse
from auth import get_current_user ,get_user_exception

app = FastAPI()






models.Base.metadata.create_all(bind=engine)

def get_db_connection():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Todo(BaseModel):
    title:str
    description:str
    priority:int = Field(gt=0,lt=6,description="priority must be less than 10")
    complete:bool


@app.get("/")
async def get_all_data(db:Session=Depends(get_db_connection)):
    return db.query(models.todos).all()

@app.get("/todos/user")
async def read_all_by_user(user: dict = Depends(get_current_user),
                           db:Session=Depends(get_db_connection)):
    if user is None:
        raise get_user_exception()
    return db.query(models.todos).filter(models.todos.owner_id == user.get("id")).all()

@app.get("/todos/{todo_id}")
async def get_todo_byid(todo_id:int,db:Session=Depends(get_db_connection)):
    todo_model = db.query(models.todos).filter(models.todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise raise_HTTP_Exception()


@app.post("/")
async def add_new_todo(tdo:Todo,db:Session=Depends(get_db_connection)):
    todo_model = models.todos()
    todo_model.title = tdo.title
    todo_model.description = tdo.description
    todo_model.priority = tdo.priority
    todo_model.complete = tdo.complete

    db.add(todo_model)
    db.commit()

    return {
        'status':201,
        'transaction':'Succesful'
    }




@app.put('/{todo_id}')
def update_todo(todo_id :int ,todo:Todo,db:Session=Depends(get_db_connection)):
    todo_model = db.query(models.todos).filter(models.todos.id==todo_id).first()
    if todo_model is None:
        raise raise_HTTP_Exception()

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo_model.complete

    db.add(todo_model)
    db.commit()

    return {
        'status':201,
        'transaction':'successful'
    }

@app.delete('/{todo_id}')
async def delete_todo(todo_id:int,db:Session=Depends(get_db_connection)):
    todo_model = db.query(models.todos).filter(models.todos.id==todo_id).first()
    print(todo_model)

    if todo_model is None:
        raise raise_HTTP_Exception()

    db.query(models.todos).filter(models.todos.id == todo_id).delete()
    db.commit()

    return {
        'status': 201,
        'transaction': 'successful'
    }






def raise_HTTP_Exception():
    return HTTPException(status_code=404,detail={"The record is not found"})

"""

from fastapi import FastAPI, APIRouter,Depends
import models
from companies import dependencies
from database import engine
from routers import auth,todos
from companies import companies

from starlette.staticfiles import StaticFiles


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.mount("/static",StaticFiles(directory="static"),name="static")

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(companies.router,prefix="/companyAPIS",
                   tags=["companyapis"],
                   dependencies=[Depends(dependencies.get_token_header)],
                   responses={418:{"description":"Internal use only"}})

