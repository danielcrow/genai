import json
import os
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods




def lambda_handler(event, context):
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(credentials)
    }


