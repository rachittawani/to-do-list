import uvicorn
from fastapi import FastAPI

import db as models
from api.routes.api import router
from db import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)