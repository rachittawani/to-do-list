from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import UUID

from models.domain.todos import TodosORM
from models.schemas.todos import ToDoRequest


def read_todo(user, db: Session):
    todo_data = db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid'))).all()
    if todo_data is None:
        raise HTTPException(status_code=404, detail="No data found.")
    return todo_data


def read_todo_by_id(user, todo_id: int, db: Session):
    todo_response = (db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
                     .filter(TodosORM.id == todo_id).first())
    if todo_response is None:
        raise HTTPException(status_code=404, detail="To do not found.")
    return todo_response


def create_todo_task(data: ToDoRequest, uuid: UUID, db: Session):
    todo_model = TodosORM(**data.dict(), owner_uuid=uuid)

    db.add(todo_model)
    db.commit()


def update_todo_task(data: ToDoRequest, user, todo_id: int, db: Session):
    todo_response = (db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
                     .filter(TodosORM.id == todo_id).first())
    if todo_response is None:
        raise HTTPException(status_code=404, detail="To do data found.")

    todo_response.title = data.title
    todo_response.description = data.description
    todo_response.priority = data.priority
    todo_response.complete = data.complete

    db.add(todo_response)
    db.commit()


def delete_todo_task(user, todo_id: int, db: Session):
    todo_response = (db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
                     .filter(TodosORM.id == todo_id).first())
    if todo_response is None:
        raise HTTPException(status_code=404, detail="To do data found.")

    db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid'))).filter(TodosORM.id == todo_id).delete()
    db.commit()
