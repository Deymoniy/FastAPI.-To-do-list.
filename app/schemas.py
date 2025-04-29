#Schemas are for visual representation of your api.
from pydantic import BaseModel
from typing import List, Optional


class Task(BaseModel):
    category: str
    title: str
    body: str 
    status: bool

class User(BaseModel):
    name:str
    email:str 
    password:str


class ShowUser(BaseModel):
    name:str
    email:str
    tasks: List[Task]
    class Config:
        from_attributes = True 

class ShowTask(Task):
    title: str
    body:str
    creator: ShowUser
    creation_date: str
    id: int
    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    category: str
    title: str
    body: str
    status: bool

class Login(BaseModel):
    mail: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None