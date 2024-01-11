
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

def getOpps():
    #return os.getenv("OPPS")
    #print( json.loads(os.getenv("OPPS")))
    return [{"OppId":"01010101",  "CustomerName":"Daniel Crow", "OpportunityName": "RB-Phantom"},{"OppId":"01010102",  "CustomerName":"Douglas Coombs", "OpportunityName": "Spectre"}]