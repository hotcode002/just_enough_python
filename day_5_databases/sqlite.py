import sqlite3

conn = sqlite3.connect("employee.db")

cur = conn.cursor()

cur.execute('''CREATE table employees (
               first text,
               last text,
               pay integer )''')

# cur.execute('''insert into employees values ('Ajay','Tech',50000)''')
cur.execute('''insert into employees values (?,?,?)''',
            ('Siva', 'Prasad', 50000))

result = cur.execute('''select * from employees''')

print(result)
print(result.fetchall())

conn.commit()
conn.close()
