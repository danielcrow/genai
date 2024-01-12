from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.genai.hr import jobinterviews
from app.genai.watsonx import watsonx
from app.police import police
from app.carsales import carsales
from app.utils.utils import custom_openapi
import json


app = FastAPI()



app.include_router(jobinterviews.router)
app.include_router(watsonx.router)
app.include_router(police.router)
app.include_router(carsales.router)


class Message(BaseModel):
    message: str

@app.get("/health")
async def root() -> Message:
    return {"message": "OK"}

openapi = custom_openapi(app)
#app.openapi = openapi
