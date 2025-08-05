#เชื่อมต่อกับ MSSQL ผ่าน pyodbc

import pyodbc
import os

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=YOUR_SERVER_NAME;'
        'DATABASE=YOUR_DB_NAME;'
        'PWD=YOUr_PASSWORD'
    )
    return conn