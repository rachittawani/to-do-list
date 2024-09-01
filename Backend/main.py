from fastapi import FastAPI

import db as models
from db import engine
from api.routes.api import router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

