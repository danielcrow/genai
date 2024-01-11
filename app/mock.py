
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

def getOpps():
    #return os.getenv("OPPS")
    #print( json.loads(os.getenv("OPPS")))
    return [{"OppId":"01010101",  "CustomerName":"Daniel Crow", "OpportunityName": "RB-Phantom"},{"OppId":"01010102",  "CustomerName":"Douglas Coombs", "OpportunityName": "Spectre"}]

def getOppDetails(OppId):
    if(OppId == "01010101"):
        return {"OppId":"01010101",  "CustomerName":"Daniel Crow", "OpportunityName": "RB-Phantom","Contact":"ABC123","Model": "Phantom", "CloseDate":"12/03/2024","VehicleType":"New","Stage":"New"}
    else:
        return {"OppId":"01010102",  "CustomerName":"Douglas Coombs", "OpportunityName": "Spectre","Contact":"ABD123","Model": "Spectre", "CloseDate":"12/05/2024","VehicleType":"New","Stage":"New"}
    
def getContactDetails(Contact):
    if(Contact == "ABC123"):
        return {"Contact":"ABC123",  "CustomerName":"Daniel Crow", "EmailAddress": "daniel.j.crow@gmail.com","Likes":"Football, Triathlon"}
    else:
        return {"Contact":"01010102",  "CustomerName":"Douglas Coombs","EmailAddress": "douglas.coombs@gmail.com","Likes":"Football, Wine"}
 

    