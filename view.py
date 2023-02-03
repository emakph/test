import sqlite3

#Database connection
conn = sqlite3.connect('students.db')

#Cursor object to execute database query
c = conn.cursor()

listToFind = input('Enter list: ')

query = 'SELECT list FROM tblstudent WHERE list=?'
c.execute(query, (listToFind,))
print(c.fetchall())

#To close database connection
conn.close()