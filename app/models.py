from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Tasks(Base):
    __tablename__='tasks'
    id = Column(Integer, primary_key=True, index = True)
    category = Column(String)
    title = Column(String)
    body = Column(String)
    status = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    creation_date = Column(String)
    creator = relationship("User", back_populates="tasks")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    tasks = relationship("Tasks", back_populates= "creator")




