# pip install pymysql

import pymysql

conn = pymysql.connect(host="localhost",
                       user="ajaytech",
                       passwd="Ajaytech@123")

cur = conn.cursor()
cur.execute('SELECT  first_name, last_name from sakila.customer')

for first_name, last_name in cur.fetchall():
    print(first_name, last_name)
