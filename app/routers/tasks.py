from typing import List
from fastapi import APIRouter, Depends, status
from app import schemas, database, oauth2
from sqlalchemy.orm import Session
from datetime import datetime
from app.repository import tasks

router = APIRouter(
    prefix="/Task",
    tags = ["Tasks"]
)

@router.get('/', response_model=List[schemas.ShowTask])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tasks.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Task, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tasks.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tasks.destroy(id, db)

@router.get('/{id}', status_code= 200, response_model=schemas.ShowTask)
def find(id: int, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tasks.find(id, db)

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowTask)
def update_id(id:int, task_data: schemas.TaskUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tasks.update_id(id, task_data, db)