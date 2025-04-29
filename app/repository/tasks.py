from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import app.schemas

def get_all(db:Session):
    tasks = db.query(models.Tasks).all()
    return tasks

def create(request: schemas.Task, db:Session):
    new_task = models.Tasks(category = request.category, status = request.status,title=request.title, body = request.body, user_id = 1, creation_date = datetime.now().strftime("%Y.%d.%m %H:%M"))
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def destroy(id: int, db: Session):
    task = db.query(models.Tasks).filter(models.Tasks.id ==id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Task with id {id} wasn't found")
    task.delete(synchronize_session=False)
    db.commit()
    return 'done'

def find(id: int, db: Session):
    task = db.query(models.Tasks).filter(models.Tasks.id == id).first(  )
    return task

def update_id(id: int, task_data: schemas.TaskUpdate, db: Session):
    task = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Task with id {id} wasn't found")
    task.category = task_data.category
    task.title = task_data.title
    task.body = task_data.body
    task.status = task_data.status

    db.commit()
    db.refresh(task)
    return task