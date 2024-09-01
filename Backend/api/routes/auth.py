from datetime import timedelta
from typing import Annotated
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

from db.users import authenticate_user
from api.dependencies.database import get_db
from api.dependencies.auth import create_access_token
from models.schemas.users import Token

router = APIRouter()



@router.post("/token", response_model=Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    token = create_access_token(user.username, user.uuid, user.role, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'Bearer'}
