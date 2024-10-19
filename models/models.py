from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database.db import engine

from models.base_model import BaseModel


class Post(BaseModel):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', backref='user')


BaseModel.metadata.create_all(engine)
