import pyodbc
import os
from dotenv import load_dotenv

def connect_to_db():
    #Connector Info
    DRIVER = 'SQL Server'
    SERVER = 'localhost'
    DB = 'NBA_Match_Simulator'
    #We load enviorment variables of the project from .env file (for security reasons) 
    load_dotenv()
    UID = os.getenv('DB_UID')
    PSW = os.getenv('DB_PSW')

    str_connection = 'DRIVER={'+DRIVER+'};SERVER='+SERVER+';DATABASE='+DB+';UID='+UID+';PWD='+PSW
    #print(str_connection)

    conn_2 = pyodbc.connect(str_connection)
    return conn_2

