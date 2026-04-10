import mysql.connector
import os

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="sentinel_aiops"
)
