from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.domain.todos import TodosORM


def read_all_as_admin(db: Session):
    read_all = db.query(TodosORM).all()
    if read_all is None:
        raise HTTPException(status_code=404, detail="No data found.")
    return read_all


def delete_to_by_id(todo_id: int, db: Session):
    todo_model = db.query(TodosORM).filter(TodosORM.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="No data found.")

    db.query(TodosORM).filter(TodosORM.id == todo_id).delete()
    db.commit()