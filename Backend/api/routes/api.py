from fastapi import APIRouter

from api.routes import (
    todos,
    auth,
    admin,
    users
)

router = APIRouter(prefix='/api')
router.include_router(auth.router, tags=['Authentication'], prefix='/auth')
router.include_router(todos.router, tags=['To Do'], prefix='/todo')
router.include_router(admin.router, tags=['Admin'], prefix='/admin')
router.include_router(users.router, tags=['Users'], prefix='/users')
