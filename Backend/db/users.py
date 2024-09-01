from uuid import UUID

from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.domain.users import UsersORM
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def create_user(user: UsersORM, db: Session):
    create_user_response = UsersORM(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=bcrypt_context.hash(user.password),
        phone_number=user.phone_number,
        is_active=True,
        role=user.role
    )

    db.add(create_user_response)
    db.commit()


def authenticate_user(username: str, password: str, db: Session):
    user = db.query(UsersORM).filter(UsersORM.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def get_all_user(user, db: Session):
    user_model = db.query(UsersORM).filter(UsersORM.uuid == UUID(user.get('uuid'))).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="No user found.")
    return user_model


def update_password(user, user_verification, db: Session):
    user_model = db.query(UsersORM).filter(UsersORM.uuid == UUID(user.get('uuid'))).first()

    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Error on password change.")

    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()
