from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

class Opp(BaseModel):
    OppId:str
    CustomerName:str
    OpportunityName:str
    
class Opps(BaseModel):
    opps: List[Opp]
    
class OppDetails(BaseModel):
    OppId:str
    CustomerName:str
    OpportunityName:str
    Contact:str
    Model:str
    CloseDate:str
    VehicleType:str
    Stage:str
    
class ContactDetails(BaseModel):
    Contact:str
    CustomerName:str
    EmailAddress:str
    Likes:str
    
class CarSpec(BaseModel):
    OppId: str  
    CarModel: str
    CarValue: float
    
class ContactHistory(BaseModel):
    Contact: str
    CustomerName: str
    PreviousBuyer: bool
    PreviousCar: str
