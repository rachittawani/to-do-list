from sqlalchemy import ForeignKey

from .users import UsersORM

owner_uuid_fk = ForeignKey('users.uuid')
