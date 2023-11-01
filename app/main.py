import string
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from app.genai import get_details

host="https://genai.1970c02pqord.eu-gb.codeengine.appdomain.cloud/"


class Message(BaseModel):
    message: str



app = FastAPI()
security = HTTPBasic()

def custom_openapi():
    
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="DC-WatsonX.ai Recruitment",
        version="1.0.0",
        description="Recruitment",
        openapi_version="3.0.0",
        routes=app.routes,
    )
    openapi_schema["servers"] = [ {
      "url": "https://{url}",
      "variables": {
        "url": {
          "default": "genai.1970c02pqord.eu-gb.codeengine.appdomain.cloud",
        }
      }
    }]
 
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi

@app.get("/getQuestions",summary="Get Sample Interview Questions",description="Get Sample Interview Questions", operation_id="GetRecruitmentQuestions")
def root(question:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> Message:
    value = get_details(question)
    return {"message": value}


