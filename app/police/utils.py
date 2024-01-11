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