from fastapi import  FastAPI , Depends , HTTPException , status , Path
from pydantic import BaseModel , Field
from typing import Annotated
from models import Todos , Base
from sqlalchemy.orm import Session
from database import engine , SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

class ToDoRequest(BaseModel):
    title:str = Field(min_length=3)
    description:str = Field(min_length=3,max_length=100)
    priority:int = Field(gt=0,lt=6)
    complete:bool


db_dependency = Annotated[Session,Depends(get_db)]
@app.get("/")
async def read_all(db:db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_od}",status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency,todo_id:int = Path(gt=0)):

    todo_model = db.query(Todos).filter(Todos.id==todo_id).first()

    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code=404,detail="Id not found")


@app.post("/todo/",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request: ToDoRequest):
    todo_model = Todos(**todo_request.dict())
    db.add(todo_model)
    db.commit()

@app.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_an_todo(db:db_dependency,todo_id:int,todo_request:ToDoRequest):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='todo not found')

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id==todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404,detail="Todo id not found")

    db.query(Todos).filter(Todos.id==todo_id).delete()
    db.commit()


