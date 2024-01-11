from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel



class Crime(BaseModel):
    CrimeId:str
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
    
    