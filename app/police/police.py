from fastapi import Depends, Request, APIRouter
from fastapi import security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import psycopg2
from pydantic import BaseModel
from app.police.policemodel import Crimes, Locations
from app.police.utils import getConnection
from app.utils.utils import getExtendedTags
import os

security = HTTPBasic()
router = APIRouter(dependencies=[Depends(security)])
extendedTags = getExtendedTags()

@router.get("/getCrimeAreasAndType",response_model=Crimes,summary="Get Crime Area and Type", description="Get Crime Area and Type", operation_id="GetCrimeAreaAndType",openapi_extra=extendedTags)
def get_crimes_type(location:str,type:str):
    try:
        conn = getConnection()


        sql = "select * from public.\"Crimes\" where lsoaname ~ '" + location+ "' and crimetype='" + type +"';"
        #sql = "select * from public.\"Crimes\" where fallswithin like %s;"
        print(sql)
        cur = conn.cursor()

        cur.execute(sql)
        rows = cur.fetchall()
        crimes = []
        print("The number of parts: ", cur.rowcount)
        for row in rows:
      
            crime = {"CrimeId": row[1], "Month": row[2],"PoliceForce": row[3],"Location": row[7],"CrimeDetails": row[10], "LastAction": row[11]}
  
            crimes.append(crime)
        cur.close()
        return {"items": crimes }
        
    except (Exception, psycopg2.DatabaseError) as error:
        raise Exception
    
    finally:
        if conn is not None:
            conn.close()
            
            
@router.get("/getCrimeAreas",response_model=Locations, summary="Get Crime Area", description="Get Crime area", operation_id="GetCrimeArea",openapi_extra=extendedTags)
def get_crime_location():
    try:
        conn = getConnection()
        sql = "select distinct lsoaname  from public.\"Crimes\""
        print(sql)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        locations = []
        for row in rows:
            location = {"location": row[0][:-5]}
            locations.append(location)
         
       
        cur.close()
        return {"locations": locations }   
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

@router.get("/getCrimes",summary="Get Crimes by Area", description="Get Crimes by area", operation_id="GetCrimesByArea",openapi_extra=extendedTags)
def get_crimes(location:str):
    try:
        conn = getConnection()


        sql = "select * from public.\"Crimes\" where lsoaname ~ '" + location+ "';"
        #sql = "select * from public.\"Crimes\" where fallswithin like %s;"
        print(sql)
        cur = conn.cursor()

        cur.execute(sql)
        rows = cur.fetchall()
        crimes = []
        print("The number of parts: ", cur.rowcount)
        for row in rows:
      
            crime = {"CrimeId": row[1], "Month": row[2],"PoliceForce": row[3],"Location": row[7],"CrimeDetails": row[10], "LastAction": row[11]}
  
            crimes.append(crime)
        cur.close()
        return {"items": crimes }
        
    except (Exception, psycopg2.DatabaseError) as error:
        raise Exception
    
    finally:
        if conn is not None:
            conn.close()