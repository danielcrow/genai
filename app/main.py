import string
from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from app.genai import get_details

class Message(BaseModel):
    message: str


app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI",
        version="1.0.0",
        openapi_version="3.0.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@app.get("/getQuestions")
def root(question ) -> Message:
    value = get_details(question)
    return {"message": value}


