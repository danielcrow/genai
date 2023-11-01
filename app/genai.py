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
        model_id=ModelTypes.FLAN_UL2,
        params=params,
        credentials=credentials,
        project_id=project_id
    )
    return model


def get_details(data):
    prompt = f"""Create some content from the information\\n\\nInput:\\nCreate a set of interview questions to ask a """ + data + """\\n\\nOutput:\\n"""

    response = model.generate(prompt)
    summary = response['results'][0]['generated_text']

    
    return summary

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

model = getModel()