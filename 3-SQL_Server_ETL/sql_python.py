import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

server = os.environ.get("MSSQL_SERVER")
database = "mockclient_saphal"
username = os.environ.get("MSSQL_USERNAME")
password = os.environ.get("MSSQL_PASSWORD")
try:
    cnxn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + server
        + ";DATABASE="
        + database
        + ";UID="
        + username
        + ";PWD="
        + password
    )
    cursor = cnxn.cursor()
    cursor.execute("SELECT name FROM sys.databases;")
    row = cursor.fetchall()
    print("[+] Connected !")
    print(row)
except Exception as e:
    print("[-] cannot connect : ", e)
