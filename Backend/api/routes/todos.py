from uuid import UUID

from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated

from models.schemas.todos import ToDoRequest
from db.todos import (
    read_todo,
    read_todo_by_id,
    create_todo_task,
    update_todo_task,
    delete_todo_task
)
from api.dependencies.database import get_db
from api.dependencies.auth import get_current_user


router = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("", status_code=status.HTTP_200_OK)
def read_all(user: user_dependency, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    return read_todo(user, db)


@router.get("/{todo_uuid}", status_code=status.HTTP_200_OK)
def read_specific_todo(user: user_dependency, todo_uuid: str, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")

    todo_by_id = read_todo_by_id(user, todo_uuid, db)
    return todo_by_id


@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo_data: ToDoRequest, user: user_dependency, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    return create_todo_task(todo_data, UUID(user.get('uuid')), db)


@router.put("/{todo_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def update_todo(todo_data: ToDoRequest,
                user: user_dependency,
                todo_uuid: str,
                db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    return update_todo_task(todo_data, user, todo_uuid, db)


@router.delete("/{todo_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user: user_dependency, todo_uuid: str, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    return delete_todo_task(user, todo_uuid, db)