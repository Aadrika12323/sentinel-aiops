import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="sentinel_aiops"
)

cursor = conn.cursor()