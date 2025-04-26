import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db as models
from api.routes.api import router
from db import engine

load_dotenv()

PORT = int(os.getenv('PORT'))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://to-do-list-inky-theta.vercel.app"],  # OR specify your frontend URL like ["https://your-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)