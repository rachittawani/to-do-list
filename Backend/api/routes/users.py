from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated

from api.dependencies.database import get_db
from api.dependencies.auth import get_current_user
from db.users import (
    get_all_user,
    update_password,
    create_user
)
from models.schemas.users import (
    UserVerification,
    CreateUserRequest
)


router = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("", status_code=status.HTTP_200_OK)
def get_user(user: user_dependency, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    return get_all_user(user, db)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_users(create_user_request: CreateUserRequest, db: Session = Depends(get_db)):
    return create_user(create_user_request, db)


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
def change_password(user: user_dependency, user_verification: UserVerification, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    return update_password(user, user_verification, db)