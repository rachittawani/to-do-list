from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import UUID

from models.domain.todos import TodosORM
from models.domain.link import LinkORM
from models.schemas.todos import ToDoRequest


def read_todo(user, db: Session):
    todo_data = db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid'))).all()
    if todo_data is None:
        raise HTTPException(status_code=404, detail="No data found.")
    joined_data = (
        db.query(TodosORM, LinkORM.name, LinkORM.hex_color, LinkORM.uuid)
        .outerjoin(LinkORM, TodosORM.list_details_uuid == LinkORM.uuid)
        .filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
        .all()
    )

    response_data = []
    for todo, name, hex_color, uuid in joined_data:
        todo_dict = {
            "title": todo.title,
            "uuid": todo.uuid,
            "priority": todo.priority,
            "due_date": todo.due_date,
            "complete": todo.complete,
            "description": todo.description,
        }
        if name and hex_color:
            todo_dict["list_details"] = {
                "name": name,
                "hex_color": hex_color,
                "list_details_uuid": uuid
            }

        response_data.append(todo_dict)
    return response_data


def read_todo_by_id(user, todo_uuid: str, db: Session):
    todo_response = (db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
                     .filter(TodosORM.uuid == todo_uuid).first())
    if todo_response is None:
        raise HTTPException(status_code=404, detail="To do not found.")

    joined_data = (
        db.query(TodosORM, LinkORM.name, LinkORM.hex_color, LinkORM.uuid)
        .outerjoin(LinkORM, TodosORM.list_details_uuid == LinkORM.uuid)
        .filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
        .filter(TodosORM.uuid == todo_uuid)
        .all()
    )

    response_data = []
    for todo, name, hex_color, uuid in joined_data:
        todo_dict = {
            "title": todo.title,
            "uuid": todo.uuid,
            "priority": todo.priority,
            "due_date": todo.due_date,
            "complete": todo.complete,
            "description": todo.description,
        }
        if name and hex_color:
            todo_dict["list_details"] = {
                "name": name,
                "hex_color": hex_color,
                "list_details_uuid": uuid
            }

        response_data.append(todo_dict)
    return response_data


def create_todo_task(data: ToDoRequest, uuid: UUID, db: Session):
    todo_model = TodosORM(**data.dict(), owner_uuid=uuid)

    db.add(todo_model)
    db.commit()


def update_todo_task(data: ToDoRequest, user, todo_uuid: str, db: Session):
    todo_response = (db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
                     .filter(TodosORM.uuid == todo_uuid).first())
    if todo_response is None:
        raise HTTPException(status_code=404, detail="To do data found.")

    todo_response.title = data.title
    todo_response.description = data.description
    todo_response.priority = data.priority
    todo_response.complete = data.complete
    if data.list_details_uuid:
        todo_response.list_details_uuid = data.list_details_uuid
    else:
        todo_response.list_details_uuid = None

    db.add(todo_response)
    db.commit()


def delete_todo_task(user, todo_uuid: str, db: Session):
    todo_response = (db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
                     .filter(TodosORM.uuid == todo_uuid).first())
    if todo_response is None:
        raise HTTPException(status_code=404, detail="No data found.")

    db.query(TodosORM).filter(TodosORM.owner_uuid == UUID(user.get('uuid'))).filter(TodosORM.uuid == todo_uuid).delete()
    db.commit()
