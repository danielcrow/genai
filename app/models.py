from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel




class NotificationItem(BaseModel):
    name: str
    type: str
    details: Dict[str, Any]


class Details(BaseModel):
    id: Optional[str] = None
    rank: Optional[int] = None
    time: Optional[int] = None
    policyId: Optional[str] = None
    subsumedUnions: Optional[List] = None
    notification: Optional[List[NotificationItem]] = None
    policyExecutionOrder: Optional[int] = None


class Insight(BaseModel):
    id: str
    type: str
    source: Optional[str] = None
    details: Details


class Item(BaseModel):
    id: str
    createdBy: str
    title: str
    description: str
    priority: int
    state: str
    owner: str
    team: str
    createdTime: str
    lastChangedTime: str
    insights: List[Insight]
    alertIds: List[str]
    contextualAlertIds: List[str]


class Incidents(BaseModel):
    items: List[Item]


class Crime(BaseModel):
    Month: str
    PoliceForce:str
    Location:str
    CrimeDetails: str
    LastAction:str
       
class Crimes(BaseModel):
    items: List[Crime]
    
    
class Location(BaseModel):
    location: str
    
class Locations(BaseModel):
    locations: List[Location]
    
    
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
    