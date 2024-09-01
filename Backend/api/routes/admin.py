from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated

from api.dependencies.auth import get_current_user
from api.dependencies.database import get_db
from db.admin import (
    read_all_as_admin,
    delete_to_by_id
)


router = APIRouter()

user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get('/todo', status_code=status.HTTP_200_OK)
def read_all(user: user_dependency, db: Session = Depends(get_db)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')

    return read_all_as_admin(db)

@router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user: user_dependency, todo_id: int = Path(gt=0), db: Session = Depends(get_db)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')

    return delete_to_by_id(todo_id, db)
