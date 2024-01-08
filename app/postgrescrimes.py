from dotenv import load_dotenv, find_dotenv
import os
import psycopg2




load_dotenv(find_dotenv())


def getConnection():
    host = os.getenv("PSQL_HOST", None)
    db = os.getenv("PSQL_DB", None)
    uid = os.getenv("PSQL_UID", None)
    pwd = os.getenv("PSQL_PWD", None)
    
    conn = psycopg2.connect(
            host=host,
            database=db,
            user=uid,
            password=pwd)
    return conn

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
      
            crime = {"Month": row[2],"PoliceForce": row[3],"Location": row[7],"CrimeDetails": row[10], "LastAction": row[11]}
  
            crimes.append(crime)
        cur.close()
       
        return crimes
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


        
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
        return locations    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




