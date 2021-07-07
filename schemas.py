"""
Author: Abdur Rehman
"""
from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    """
    schema for data parsing and validation
    :params BaseModel
    """
    title: str
    description: str
