from sqlalchemy import Column, Integer, String, Boolean, PickleType, Date, ForeignKey
from fastapi_utils.guid_type import GUID
from uuid import uuid4

from db import Base
# from .associations import owner_uuid_fk

class TodosORM(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, default=uuid4, unique=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    due_date = Column(Date)
    list_details_uuid = Column(GUID, ForeignKey('link.uuid'), nullable=True)
    owner_uuid = Column(GUID, ForeignKey('users.uuid'))
