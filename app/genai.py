import json
import os
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from dotenv import load_dotenv

import requests

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
    question = summary
    #print(question)
    return question

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
    question = summary
    #print(question)
    return question

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

def callRAG(apikey:str, question:str, projectid:str):
    
    
    reqUrl = "http://141.125.105.231:3000/api/generate?input=" + question + "&project_id=" + projectid
    headersList = {
            "Accept": "*/*",
            "x-api-key": apikey
                
        }
   
    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    jsonvalue = response.json()
    jdump = json.dumps(jsonvalue)
    jsonvalue = json.loads(jdump)
    print(jsonvalue["generated_text"])
    return jsonvalue["generated_text"]
  