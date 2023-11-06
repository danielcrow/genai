import string
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.utils import get_openapi
from fastapi import File, UploadFile

from pydantic import BaseModel
from app.genai import get_details

host="genai.1970c02pqord.eu-gb.codeengine.appdomain.cloud"
#host="localhost:8000"

protocol="https"

class Message(BaseModel):
    question: list[str]

svgimage=f"""<svg xmlns="http://www.w3.org/2000/svg" id="OpenSearchicon" viewBox="0 0 100 100"> 
  <defs> 
    <linearGradient x1="0.085" y1="0.085" x2="0.915" y2="0.915" id="OpenSearchg">
      <stop offset="0" stop-color="#1417cc" stop-opacity="1"/>
      <stop offset="0.5" stop-color="#1517cc" stop-opacity="0"/>
      <stop offset="1" stop-color="#1517cc" stop-opacity="1"/>
    </linearGradient>
  </defs>
  <g transform="scale(0.39)">
  <rect width="256" height="256" rx="55" ry="55" x="0" y="0" fill="#1517cc"/>
  <rect width="246" height="246" rx="50" ry="50" x="5" y="5" fill="#5252f4"/>
  <rect width="236" height="236" rx="45" ry="45" x="10" y="10" fill="url(#OpenSearchg)"/>
  <path fill="none" stroke="#fff" stroke-width="26" d="M 178 103 A 74 74 0 1 1  30,103 A 74 74 0 1 1  178 103 z" transform="matrix(0.918696,0,0,0.918696,4.331024,5.50348)"/>
  <rect fill="#fff" stroke="none" width="102.33237" height="39.089138" x="211.87753" y="-19.544645" transform="matrix(0.707107,0.707107,-0.707107,0.707107,0,0)"/>
  </g>
</svg>"""

extendedTags = {"x-ibm-application-icon":svgimage}

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
      "url": protocol+ "//" + host +"/",
    }]
 
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi

@app.get("/getQuestions",summary="Get Sample Interview Questions", description="Get Sample Interview Questions", operation_id="GetRecruitmentQuestions",openapi_extra=extendedTags)
def root(question:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> Message:
    value = get_details(question)
    print(value)
    return {"question": value}


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile)-> str:
    return "filename" + file.filename