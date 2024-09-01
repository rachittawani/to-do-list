from sqlalchemy import Column, Integer, String, Boolean
from uuid import uuid4
from fastapi_utils.guid_type import GUID

from db import Base

class UsersORM(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, default=uuid4, unique=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
