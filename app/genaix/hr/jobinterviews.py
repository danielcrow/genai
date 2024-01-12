from fastapi import Depends, Request, APIRouter
from fastapi import security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from app.utils.utils import getExtendedTags,getModel
import os

security = HTTPBasic()
router = APIRouter(dependencies=[Depends(security)])
extendedTags = getExtendedTags()

class Message(BaseModel):
    question: list[str]


@router.get("/getQuestions",response_model=Message, summary="Get Sample Interview Questions", description="Get Sample Interview Questions", operation_id="GetRecruitmentQuestions",openapi_extra=extendedTags)
def jobinterviews(role:str, request:Request):
    model = getModel("ibm/granite-13b-chat-v1")
    
    
    
    prompt = f"""Create job interviews based on role.Input:Create 10 interview questions to ask the role of """ + role + """ Output:"""
    print(prompt)
    response = model.generate(prompt)
    #print(response)
    summary = response['results'][0]['generated_text']

    question = summary.split("?")
    return {"question": question}
   