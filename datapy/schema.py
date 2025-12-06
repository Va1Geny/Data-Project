import os
import mysql.connector
from dotenv import load_dotenv

mydb = mysql.connector.connect(
    host="db_host",
    user="db_user",
    password="db_pass"
)

mycursor = mydb.cursor()

mycursor.execute(
    "create database if not exists bankmodel")
