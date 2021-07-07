"""
Author: Abdur Rehman
"""
from typing import Optional
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, exc
from models import Todo
from schemas import CreateTodoRequest
from database import get_db


app = FastAPI()


@app.post("/")
def create(details: CreateTodoRequest, db_obj: Session = Depends(get_db)):
    """
    post obj api call
    :params details
    :params db_obj
    """
    try:
        to_create = Todo(
            title=details.title,
            description=details.description
        )
        db_obj.add(to_create)
        db_obj.commit()
        return {"success": True, "created_id": to_create.id}
    except exc.ObjectDereferencedError as ex:
        return {"success": False, "message": str(ex)}


@app.delete("/")
def delete(task_id: int, db_obj: Session = Depends(get_db)):
    """
    delete obj api call
    :param task_id: int
    :param db_obj: object
    :return: response
    """
    db_obj.query(Todo).filter(Todo.id == task_id).delete()
    db_obj.commit()
    return {"success": True}


@app.get("/")
def get(task_id: Optional[int] = None, db_obj: Session = Depends(get_db)):
    """
    get all objects and single object api call
    :param task_id: int
    :param db_obj: object
    :return: response
    """
    try:
        if task_id:
            return db_obj.query(Todo).filter(Todo.id == task_id).first()
        return db_obj.query(Todo).all()
    except exc.ObjectDereferencedError as ex:
        return {"success": False, "message": str(ex)}


@app.post("/task_id")
def update_task(task_id: int, title: str, description: str, db_obj: Session = Depends(get_db)):
    """
    update object api call
    :param task_id: int
    :param title: str
    :param description: str
    :param db_obj: object
    :return: response
    """
    try:
        task_obj = db_obj.query(Todo).filter(Todo.id == task_id)
        task_obj.update({'title': title, 'description': description})
        db_obj.commit()
        return {"success": True, "message": "Task has been updated successfully"}
    except exc.ObjectDereferencedError as ex:
        return {"success": False, "message": str(ex)}
