import json
import os
from fastapi.openapi.utils import get_openapi
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from dotenv import load_dotenv, find_dotenv

import requests

load_dotenv(find_dotenv())

def getModel():

    credentials = setEnviroment()
    project_id=os.getenv("PROJECT_ID", None)
   
    print(project_id)
    params = {
        GenParams.DECODING_METHOD: "sample",
        GenParams.MAX_NEW_TOKENS: 500,
        GenParams.MIN_NEW_TOKENS: 100,
        GenParams.TEMPERATURE: 0,
        GenParams.TOP_K: 50,
        GenParams.TOP_P: 0
    }
    model = Model(
        model_id="ibm/granite-13b-chat-v1",
        #model_id=ModelTypes.FLAN_UL2,
        params=params,
        credentials=credentials,
        project_id=project_id
    )
    return model

def getModel(model:str):
  
    credentials = setEnviroment()
 
    project_id=os.getenv("PROJECT_ID", None)
    print(project_id)
    params = {
        GenParams.DECODING_METHOD: "sample",
        GenParams.MAX_NEW_TOKENS: 500,
        GenParams.MIN_NEW_TOKENS: 100,
        GenParams.TEMPERATURE: 0,
        GenParams.TOP_K: 50,
        GenParams.TOP_P: 0
    }
    model = Model(
        model_id=model,
        #model_id=ModelTypes.FLAN_UL2,
        params=params,
        credentials=credentials,
        project_id=project_id
    )
    return model


def setEnviroment():
     # TODO implement

    api_key=os.getenv("GENAI_KEY", None)

    api_endpoint=os.getenv("GENAI_API_ENDPOINT", None)
    project_id=os.getenv("PROJECT_ID", None)
    credentials={
        "apikey": api_key,
        "url": api_endpoint
    }
    return credentials

def getExtendedTags():
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
    return extendedTags

def custom_openapi(app):
    
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Sales",
        version="1.0.0",
        description="Sales",
        openapi_version="3.0.0",
        routes=app.routes,
    )

    openapi_schema["servers"] = [{
        "url":"https://genai.1970c02pqord.eu-gb.codeengine.appdomain.cloud"},
        {"url":"http://localhost:8000"
    }]
    app.openapi_schema = openapi_schema
  
    return app.openapi_schema