import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os

import db as models
from api.routes.api import router
from db import engine

load_dotenv()

PORT = int(os.getenv('PORT'))

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)