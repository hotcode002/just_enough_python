# Make sure you don't name this file as mysql.py

import mysql.connector


conn = mysql.connector.connect(user='ajaytech', password='Ajaytech@123',
                               host='localhost',
                               database='sakila')

cursor = conn.cursor()

cursor.execute("select first_name, last_name from sakila.customer")

for (first_name, last_name) in cursor:
    print(first_name, last_name)

conn.close()
