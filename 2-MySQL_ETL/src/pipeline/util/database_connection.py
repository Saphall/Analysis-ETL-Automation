import os
import pymysql.cursors
from util.color_codes import *
from dotenv import load_dotenv
from pymysql.constants import CLIENT

load_dotenv()

host = os.environ.get("MYSQL_SERVER")
user = os.environ.get("MYSQL_USERNAME")
password = os.environ.get("MYSQL_PASSWORD")


def databaseConnect(database=""):
    """
    This function helps to connect to mysql database.
    """
    try:
        return pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            client_flag=CLIENT.MULTI_STATEMENTS,
            cursorclass=pymysql.cursors.DictCursor,
        )
    except Exception as e:
        print(f"{FAILURE}[-] Exception Occured:{END}", e)


def databaseDisconnect(connection, cursor):
    """
    This function helps to disconnect from database.
    """
    try:
        connection.close()
        cursor.close()
    except Exception as e:
        print(f"{FAILURE}[-] Exception Occured:{END}", e)
