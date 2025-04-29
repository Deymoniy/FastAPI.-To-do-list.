from fastapi import APIRouter,Depends, status
from app import database, schemas, hashing
from sqlalchemy.orm import Session
from app.repository import user

router = APIRouter(
    prefix = "/user",
    tags = ['Users']
)

get_db = database.get_db

@router.post('/', response_model= schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', status_code= status.HTTP_200_OK, response_model= schemas.ShowUser)
def show(id, db: Session = Depends(get_db)):
    return user.show(id, db)