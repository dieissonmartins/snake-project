import os
import mysql.connector
from dotenv import load_dotenv
import logging

load_dotenv()

host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

try:
    con = mysql.connector.connect(host=host, database=database, user=user, password=password)

    if con.is_connected():
        db_info = con.get_server_info()

        print('connection TRUE - ', db_info)

        cursor = con.cursor()

        cursor.execute("select database();")
        row = cursor.fetchone()

        logging.info("connected to the database", row)

except:
    logging.error("not connected to the database")
