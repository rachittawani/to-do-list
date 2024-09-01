from sqlalchemy import Column, Integer, String, Boolean
from fastapi_utils.guid_type import GUID

from db import Base
from .associations import owner_uuid_fk

class TodosORM(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_uuid = Column(GUID, owner_uuid_fk)
