from fastapi import Depends, Request, APIRouter
from fastapi import security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import psycopg2
from pydantic import BaseModel
from app.carsales.car_sales_models import ContactDetails, OppDetails, Opps
from app.utils.utils import getExtendedTags
import os

security = HTTPBasic()
router = APIRouter(dependencies=[Depends(security)])
extendedTags = getExtendedTags()

@router.get("/getContactDetails",response_model=ContactDetails, summary="Get Contact Details", description="Get Contact Details", operation_id="GetContactDetails",openapi_extra=extendedTags)
def getContactDetails(Contact):
    if(Contact == "ABC123"):
        return {"Contact":"ABC123",  "CustomerName":"Daniel Crow", "EmailAddress": "daniel.j.crow@gmail.com","Likes":"Football, Triathlon"}
    else:
        return {"Contact":"ABD123",  "CustomerName":"Douglas Coombs","EmailAddress": "douglas.coombs@gmail.com","Likes":"Football, Wine"}


@router.get("/getOppDetails", response_model=OppDetails, summary="Get Opp Details", description="Get Opp Details", operation_id="GetOppDetails",openapi_extra=extendedTags)
def getOppDetails(OppId):
    if(OppId == "01010101"):
        return {"OppId":"01010101",  "CustomerName":"Daniel Crow", "OpportunityName": "Ghost","Contact":"ABC123","Model": "Ghost", "CloseDate":"12/03/2024","VehicleType":"New","Stage":"New"}
    else:
        return {"OppId":"01010102",  "CustomerName":"Douglas Coombs", "OpportunityName": "Spectre","Contact":"ABD123","Model": "Spectre", "CloseDate":"12/05/2024","VehicleType":"New","Stage":"New"}
    

@router.get("/getOpps",summary="Get My Opps", response_model=Opps, description="Get My Opps", operation_id="GetMyOpps",openapi_extra=extendedTags)
def getOpps():
    return {"opps" : [{"OppId":"01010101",  "CustomerName":"Daniel Crow", "OpportunityName": "Ghost"},{"OppId":"01010102",  "CustomerName":"Douglas Coombs", "OpportunityName": "Spectre"}]}


