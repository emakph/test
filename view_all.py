import sqlite3

#Database connection
conn = sqlite3.connect('students.db')

#Cursor object to execute database query
c = conn.cursor()

query = 'SELECT * FROM tblstudent'

for row in c.execute(query):
    print(row)

conn.close()