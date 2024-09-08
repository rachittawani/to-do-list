from uuid import uuid4

from sqlalchemy import Column, Integer, String, ForeignKey
from fastapi_utils.guid_type import GUID

from db import Base


class LinkORM(Base):
    __tablename__ = 'link'

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(GUID, default=uuid4, unique=True)
    name = Column(String)
    hex_color = Column(String)
    owner_uuid = Column(GUID, ForeignKey('users.uuid'))
