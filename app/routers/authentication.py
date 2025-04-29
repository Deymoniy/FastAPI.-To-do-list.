from fastapi import APIRouter, Depends, HTTPException, status
from app import schemas, database, models, JWToken
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends (), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Invalid Credentials')
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Invalid password!"
        )
    access_token = JWToken.create_access_token(data={"sub": user.email})
    return {'access_token': access_token, "token_type": 'bearer'}