from fastapi import FastAPI
from core.config import Settings


app=FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)


@app.get("/")
def hello():
    return{"msg":"hello FastAPI"}