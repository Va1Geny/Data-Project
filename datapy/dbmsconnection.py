import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

try:
    connection = mysql.connector.connect(
        host=os.getenv('db_host'),
        user=os.getenv('db_user'),
        password=os.getenv('db_pass'),
        database="bankmodel",
        port=3306
    )

    if connection.is_connected():
        print("Connection is successful, enjoy your work.")
        print("Database:", connection.database)
except Error as e:
    print("Error while connecting:", e)
finally:
    if "connection" in locals() and connection.is_connected():
        connection.close()
