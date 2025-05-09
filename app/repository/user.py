from fastapi import status, HTTPException
from app import database, schemas, models,hashing
from sqlalchemy.orm import Session

def create_user(request: schemas.User, db: Session):
    hashedPassword = hashing.pwd_cxt.hash(request.password)
    new_user = models.User(name = request.name, email = request.email, password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f"User {id} wasn't found")
    return user