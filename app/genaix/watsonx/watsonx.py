from fastapi import Depends, Request, APIRouter
from fastapi import security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from app.utils.utils import getExtendedTags,getModel
import os

security = HTTPBasic()
router = APIRouter(dependencies=[Depends(security)])
extendedTags = getExtendedTags()


class results(BaseModel):
    result: str

@router.get("/askQuestion",response_model=results,summary="Ask WatsonX Question", description="Ask WatsonX Question", operation_id="getstandardquestion",openapi_extra=extendedTags)
def ask_question(data:str):
    model = getModel("meta-llama/llama-2-70b-chat")
    defaultPrompt = f"""[INST]<<SYS>>You are a helpful assistant that answers users questions using the data provided. The data has been provided between the "#### START OF DATA ####" and "#### END OF DATA ####" tags. The answer should never mention that you are using data to answer the question. If no relevant data has been provided you should answer "I have not been trained on that information.".<</SYS>>
        #### START OF DATA ####
        #### END OF DATA ####
        #### START OF QUESTION ####
            """ + data + """
        #### END OF QUESTION ####[/INST]
        Based on the data, the answer to the question is:"""
    
    prompt = f"""Ask a Question .Input: """ + data + """ Output:"""
    print(defaultPrompt)
    response = model.generate(defaultPrompt)
    #print(response)
    summary = response['results'][0]['generated_text']
    #print(question)
    
    question = {"result": summary}
    return question


@router.get("/generateEmail",response_model=results,summary="Ask Watson X Email", description="Ask WatsonX Email", operation_id="getstandardwxoemail",openapi_extra=extendedTags)
def generateEmail(customer:str, date:str):
    model = getModel("meta-llama/llama-2-70b-chat")
    
    defaultPrompt = f"""[INST]<<SYS>>You are a helpful assistant that answers users questions using the data provided. The data has been provided between the "#### START OF DATA ####" and "#### END OF DATA ####" tags. The answer should never mention that you are using data to answer the question. If no relevant data has been provided you should answer "I have not been trained on that information.".<</SYS>>
        #### START OF DATA ####
            Customer Name: """+ customer + """
            Offer Date: """ + date + """
            My Name: Daniel Crow
        #### END OF DATA ####
        #### START OF QUESTION ####
            Please generate Email offering a deal to a current customer
        #### END OF QUESTION ####[/INST]
        Based on the data, the answer to the question is:"""
    
    #prompt = f"""input": "generate a email\n\nGenerate an email to pitch a sales offer to an existing account.  \n\nOffer Type: Discount  \nCompany: Dan GROUP - 400 Widgets  \nOffer Date: Nov 21st 2023 \nDiscount: " """
    print(defaultPrompt)
    response = model.generate(defaultPrompt)
    #print(response)
    summary = response['results'][0]['generated_text']
    
    return {"result": summary}

@router.get("/generateContent",response_model=results, summary="Ask Watson X Content", description="Ask WatsonX Content", operation_id="getstandardwxoecontent",openapi_extra=extendedTags)
def generateContent(data:str, question:str):
    
    model = getModel("meta-llama/llama-2-70b-chat")
    
    defaultPrompt = f"""[INST]<<SYS>>You are a helpful assistant that answers users questions using the data provided. The data has been provided between the "#### START OF DATA ####" and "#### END OF DATA ####" tags. The answer should never mention that you are using data to answer the question. If no relevant data has been provided you should answer "I have not been trained on that information.".<</SYS>>
        #### START OF DATA ####
            """+ data + """
        #### END OF DATA ####
        #### START OF QUESTION ####
             """+ question + """
        #### END OF QUESTION ####[/INST]
        Based on the data, the answer to the question is:"""
    
    #prompt = f"""input": "generate a email\n\nGenerate an email to pitch a sales offer to an existing account.  \n\nOffer Type: Discount  \nCompany: Dan GROUP - 400 Widgets  \nOffer Date: Nov 21st 2023 \nDiscount: " """
    print(defaultPrompt)
    response = model.generate(defaultPrompt)
    #print(response)
    summary = response['results'][0]['generated_text']

    #print(question)
    return {"result": summary}