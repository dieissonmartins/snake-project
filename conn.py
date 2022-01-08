import mysql.connector

con = mysql.connector.connect(host='localhost', database='db_name', user='root', password='')

if con.is_nnected():
    db_info = con.get_server_info()

    print("connection TRUE - ", db_info)

    cursor = con.cursor()

    cursor.execute("select database();")
    row = cursor.fetchone()

    print("connected to the database", row)
