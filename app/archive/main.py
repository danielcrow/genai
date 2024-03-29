import string
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Request,Security
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import APIKeyHeader
from fastapi.openapi.utils import get_openapi
from fastapi import File, UploadFile
from typing import  Annotated, List,Union


from app.archive.models import Incidents,Item,Crime,Crimes,Locations,Location,Opps,OppDetails,ContactDetails

from pydantic import BaseModel, Field
from app.archive.genaiold import get_details
from app.archive.genaiold import ask_question
from app.archive.aiops import  getIncidents
from app.archive.aiops import getIncident
from app.archive.genaiold import generateEmail
from app.archive.genaiold import generateContent
from app.archive.genaiold import callRAG
from app.archive.postgrescrimes import get_crime_location
from app.archive.postgrescrimes import get_crimes
from app.archive.mock import getOpps
from app.archive.mock import getOppDetails
from app.archive.mock import getContactDetails
from app.archive.postgrescrimes import get_crimes_type


class Content(BaseModel):
    content: bytes

class results(BaseModel):
    result: str

class Message(BaseModel):
    question: list[str]
    
class Question(BaseModel):
    data: str
    question: str | None = None

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

api_key_header = APIKeyHeader(name="X-API-Key")


@app.get("/getContactDetails",summary="Get Contact Details", description="Get Contact Details", operation_id="GetContactDetails",openapi_extra=extendedTags)
async def root(Contact:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> ContactDetails:
    value = getContactDetails(Contact)
    rtnValue =  value
    
    print(rtnValue)
 
    return rtnValue

@app.get("/getOppDetails",summary="Get Opp Details", description="Get Opp Details", operation_id="GetOppDetails",openapi_extra=extendedTags)
async def root(OppId:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> OppDetails:
    value = getOppDetails(OppId)
    rtnValue =  value
    
    print(rtnValue)
 
    return rtnValue

@app.get("/getOpps",summary="Get My Opps", description="Get My Opps", operation_id="GetMyOpps",openapi_extra=extendedTags)
async def root(credentials: HTTPBasicCredentials = Depends(security)  ) -> Opps:
    value = getOpps()
    rtnValue =  {"opps": value}
    
    print(rtnValue)
 
    return rtnValue

@app.get("/getCrimes",summary="Get Crimes by Area", description="Get Crimes by area", operation_id="GetCrimesByArea",openapi_extra=extendedTags)
async def root(area:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> Crimes:
    value = get_crimes(area)
    rtnValue =  {"items": value}
    
    print(rtnValue)
 
    return rtnValue


@app.get("/getCrimeAreasAndType",summary="Get Crime Area and Type", description="Get Crime Area and Type", operation_id="GetCrimeAreaAndType",openapi_extra=extendedTags)
async def root(area:str,type:str,credentials: HTTPBasicCredentials = Depends(security)  ) -> Crimes:
    value = get_crimes_type(area,type)
    rtnValue = {"items": value }
    print(rtnValue)
    return rtnValue

@app.get("/getCrimeAreas",summary="Get Crime Area", description="Get Crime area", operation_id="GetCrimeArea",openapi_extra=extendedTags)
async def root(credentials: HTTPBasicCredentials = Depends(security)  ) -> Locations:
    value = get_crime_location()
    rtnValue = {"locations": value }
    print(rtnValue)
    return rtnValue

@app.get("/getQuestions",summary="Get Sample Interview Questions", description="Get Sample Interview Questions", operation_id="GetRecruitmentQuestions",openapi_extra=extendedTags)
async def root(question:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> Message:
    value = get_details(question)
    print(value)
    return {"question": value}

@app.get("/askQuestion",summary="Ask WatsonX Question", description="Ask WatsonX Question", operation_id="getstandardquestion",openapi_extra=extendedTags)
async def root(question:str,    credentials: HTTPBasicCredentials = Depends(security)  ) -> results:
    results = ask_question(question)
    print(results)
    return {"result": results}

@app.get("/getIncidents",summary="Get AiOps Incidents", description="Get AiOps Incidents", operation_id="getaiopsincidents",openapi_extra=extendedTags)
async def root(credentials: HTTPBasicCredentials = Depends(security)  ) -> Incidents:
    incidents:Incidents = getIncidents()
    return incidents

@app.get("/getIncident",summary="Get AiOps Incident", description="Get AiOps Incident", operation_id="getaiopsincident",openapi_extra=extendedTags)
async def root(id:str,credentials: HTTPBasicCredentials = Depends(security)  ) -> Item:
    item:Item = getIncident(id)
    return item

@app.get("/generateEmail",summary="Ask Watson X Email", description="Ask WatsonX Email", operation_id="getstandardwxoemail",openapi_extra=extendedTags)
async def root(customer:str, emaildate:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> results:
    results = generateEmail(customer,emaildate)
    print(results)
    return {"result": results}

@app.get("/generateContent",summary="Ask Watson X Content", description="Ask WatsonX Content", operation_id="getstandardwxoecontent",openapi_extra=extendedTags)
async def root(data:str, question:str, credentials: HTTPBasicCredentials = Depends(security)  ) -> results:
    results = generateContent(data,question)
    print(results)
    return {"result": results}

@app.post("/generateContent",summary="Ask Watson Xv2", description="Ask WatsonX Contentv2", operation_id="getstandardwxoecontentv2",openapi_extra=extendedTags)
async def root(question: Question, credentials: HTTPBasicCredentials = Depends(security)  ) -> results:
    results = generateContent(question.data, question.question)
    print(results)
    return {"result": results}

@app.get("/askCuratedQuestion",summary="Ask Watson X curated", description="Ask WatsonX curated", operation_id="getstandardwxoecurated",openapi_extra=extendedTags)
async def root(question:str, projectId:str) -> results:
    print("Daniel")
    results = callRAG( question,projectId)
   
    print(results)
    return {"result": results}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI",
        version="1.0.0",
        openapi_version="3.0.0",
        routes=app.routes,
    )
    openapi_schema["servers"] = [    {
      "url": "https://{url}",
      "variables": {
        "url": {
          "default": "fastapi.15tk3i02fluj.private.eu-gb.codeengine.appdomain.cloud",
        }
      }
    }]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

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

    openapi_schema["servers"] = [{
        "url":"https://genai.1970c02pqord.eu-gb.codeengine.appdomain.cloud"},
        {"url":"http://localhost:8000"
    }]
    app.openapi_schema = openapi_schema
  
    return app.openapi_schema


app.openapi = custom_openapi


