#First of all we need to import fastapi itself
from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import tasks, user, authentication


#this makes it so you don't need to right weid command an just do it via decorators.

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(tasks.router)
app.include_router(user.router)
app.include_router(authentication.router)