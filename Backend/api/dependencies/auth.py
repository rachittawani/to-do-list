import os
from datetime import timedelta, datetime, timezone
from typing import Annotated

from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from uuid import UUID

load_dotenv()

KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGO')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


def create_access_token(username: str, user_uuid: UUID, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'uuid': str(user_uuid), 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, KEY, algorithm=ALGORITHM)


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        uuid: str = payload.get('uuid')
        user_role: str = payload.get('role')
        if username is None or uuid is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")

        return {'username': username, 'uuid': uuid, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
