from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database.db import engine
from .base_model import BaseModel


class Post(BaseModel):
    __tablename__ = 'posts'

    user_name = Column(String)
    content = Column(Text)
    post_content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    edited_at = Column(DateTime, default=None)


class Comment(BaseModel):
    __tablename__ = 'comments'

    user_name = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='comments')


BaseModel.metadata.create_all(engine)
