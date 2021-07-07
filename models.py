"""
Author: Abdur Rehman
"""
from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from database import Base


class Todo(Base):
    """
    model class for todo table
    """
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String)