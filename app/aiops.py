import requests
import json
from app.models import Incidents
from app.models import Item
import os
from dotenv import load_dotenv

reqUrl = os.getenv("AIOPS_OPS_ENDPOINT", None)

zenKey = api_key=os.getenv("AIOPSZENAPI_KEY", None)

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Authorization": zenKey 
}


def getIncidents():
    payload = ""
    response = requests.request("GET", reqUrl, data=payload,  headers=headersList,verify=False)
  
    
    j = json.loads(response.text)
    u = Incidents(**j)
    print(u)
    return u

def getIncident(id:str):
    payload = ""
    print(reqUrl + "/" + id)
    response = requests.request("GET", reqUrl + "/" + id, data=payload,  headers=headersList,verify=False)
  
    print(response.json)
    j = json.loads(response.text)
    u = Item(**j)
    print(u)
    return u
