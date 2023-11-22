import json
import os
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from dotenv import load_dotenv

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

def get_details(data):
    model = getModel("ibm/granite-13b-chat-v1")
    prompt = f"""Create job interviews based on role.Input:Create 10 interview questions to ask the role of """ + data + """ Output:"""
    print(prompt)
    response = model.generate(prompt)
    #print(response)
    summary = response['results'][0]['generated_text']

    question = summary.split("?")

    #print(question)
    
    

    return question

def ask_question(data):
    model = getModel("llama-2-70b-chat")
    prompt = f"""Ask a Question .Input: """ + data + """ Output:"""
    print(prompt)
    response = model.generate(prompt)
    #print(response)
    summary = response['results'][0]['generated_text']
    question = summary
    #print(question)
    return question

def generateEmail(customer:str, date:str):
    model = getModel("llama-2-13b-chat")
    prompt = f""""input": "Generate an email to pitch a sales offer to an existing account.  \nOffer type: Discount  \nCompany: Global Media - 400 Widgets  \nOffer Date: Nov 21st 2023 \nDiscount" """
    print(prompt)
    response = model.generate(prompt)
    #print(response)
    summary = response['results'][0]['generated_text']
    question = summary
    #print(question)
    return question

def setEnviroment():
     # TODO implement
    load_dotenv()
    api_key=os.getenv("GENAI_KEY", None)
    api_endpoint=os.getenv("GENAI_API_ENDPOINT", None)
    project_id=os.getenv("PROJECT_ID", None)
    credentials={
        "apikey": api_key,
        "url": api_endpoint
    }
    return credentials

