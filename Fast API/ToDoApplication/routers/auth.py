import sys
sys.path.append("..")

"""
from fastapi import FastAPI , Depends,HTTPException,status
from typing import Optional
from pydantic import BaseModel
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from datetime import datetime,timedelta
from jose import jwt,JWTError

SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGORITHM = "HS256"


import models

class CreateUser(BaseModel):
    username:str
    email:Optional[str]
    First_name:str
    Last_name:str
    password:str

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")



app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def create_hash_password(password):
    return  bcrypt_context.hash(password)

def verify_password(plain_password,hashed_password):
    return bcrypt_context.verify(plain_password,hashed_password)

def authenticate_user(username: str,password: str,db):

    user = db.query(models.Users).filter(models.Users.username==username).first()

    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user

async def get_current_user(token:str=Depends(OAuth2PasswordBearer)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        userid: int = payload.get("id")
        print("username "+ username)
        print("userid" +userid)

        if username is None or userid is None:
            return get_user_exception()
        return {"username":username,"id":id}

    except JWTError:
        print("issue is here111111111111111")
        return get_user_exception()


def create_access_token(username: str,user_id:int,expires_delta:Optional[timedelta]=None):
    encode = {"sub":username,"id":user_id}
    if expires_delta:
        expire = datetime.utcnow() +expires_delta
    else:
        expire = datetime.utcnow()+timedelta(minutes=15)
    encode.update({"exp":expire})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

@app.post('/create/user')
async def create_new_users(create_user:CreateUser,db: Session = Depends(get_db)):
    models_create_user = models.Users()
    models_create_user.username = create_user.username
    models_create_user.email = create_user.email
    models_create_user.first_name = create_user.First_name
    models_create_user.last_name = create_user.Last_name
    hash_password = create_hash_password(create_user.password)
    models_create_user.hashed_password = hash_password
    models_create_user.is_active = True
    db.add(models_create_user)
    db.commit()
    print("Username has been successfully created")
    return models_create_user


@app.post('/token')
async def login_for_access_token(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username,user.id,expires_delta=token_expires)
    return {"token":token}

@app.get('/')
async def welcome():
    return {'welcome':'Welcome to the user page'}

#Exceptions
def get_user_exception():
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Beared"}
    )
    return  credential_exception

def token_exception():
    token_exp = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="incorrect username and passowrd",
        headers={"WWW-Authenticate": "Beared"}
    )
    return token_exp
"""

from fastapi import FastAPI, Depends, HTTPException, status,APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError


SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGORITHM = "HS256"


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter(prefix="/auth",tags=["Auth"],responses={'401':{'user':'Not authorised'}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users)\
        .filter(models.Users.username == username)\
        .first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int,
                        expires_delta: Optional[timedelta] = None):

    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")

        if username is None or user_id is None:
            raise get_user_exception()
        print(f"username: {username},id:{user_id}")
        return {"username": username, "id": user_id}
    except JWTError:
        raise get_user_exception()

@router.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name

    hash_password = get_password_hash(create_user.password)

    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username,
                                user.id,
                                expires_delta=token_expires)
    return {"token": token}


#Exceptions
def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response













