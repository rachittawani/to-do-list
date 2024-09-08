from uuid import UUID

from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated

from api.dependencies.database import get_db
from api.dependencies.auth import get_current_user
from db.link import (
    get_link_list,
    create_new_link,
    delete_link
)
from models.schemas.link import (
    CreateLinkRequest
)


router = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("", status_code=status.HTTP_200_OK)
def get_link(user: user_dependency, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    return get_link_list(user, db)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_link(create_link_request: CreateLinkRequest, user: user_dependency, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    return create_new_link(create_link_request, UUID(user.get('uuid')), db)


@router.delete("/{link_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user: user_dependency, link_uuid: str, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    return delete_link(user, link_uuid, db)