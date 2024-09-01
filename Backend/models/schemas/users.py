from typing import Optional

from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    phone_number: str
    role: Optional[str]


class Token(BaseModel):
    access_token: str
    token_type: str


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)
