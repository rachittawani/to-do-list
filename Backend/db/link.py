from fastapi import HTTPException
from uuid import UUID
from sqlalchemy.orm import Session

from models.domain.link import LinkORM
from models.domain.todos import TodosORM
from models.schemas.link import CreateLinkRequest


def get_link_list(user, db: Session):
    link_data = db.query(LinkORM).filter(LinkORM.owner_uuid == UUID(user.get('uuid'))).all()
    if link_data is None:
        raise HTTPException(status_code=404, detail="No data found.")
    return link_data


def create_new_link(data: CreateLinkRequest, uuid, db: Session):
    link_model = LinkORM(**data.dict(), owner_uuid=uuid)

    db.add(link_model)
    db.commit()


def delete_link(user, link_uuid: str, db: Session):

    link_response = (
        db.query(LinkORM)
        .filter(LinkORM.owner_uuid == UUID(user.get('uuid')))
        .filter(LinkORM.uuid == link_uuid)
        .first()
    )

    if link_response is None:
        raise HTTPException(status_code=404, detail="Link data not found.")

    todos_with_link = (
        db.query(TodosORM)
        .filter(TodosORM.owner_uuid == UUID(user.get('uuid')))
        .filter(TodosORM.list_details_uuid == link_uuid)
        .all()
    )

    for todo in todos_with_link:
        todo.list_details_uuid = None
        db.add(todo)

    db.commit()

    db.query(LinkORM).filter(LinkORM.owner_uuid == UUID(user.get('uuid'))).filter(LinkORM.uuid == link_uuid).delete()
    db.commit()

