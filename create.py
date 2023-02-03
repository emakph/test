import sqlite3

#Database connection
conn = sqlite3.connect('students.db')

#Cursor object to execute database query
c = conn.cursor()

#Database query to create table and columns
query = 'CREATE TABLE IF NOT EXISTS tblstudent (name text, age integer)'
c.execute(query)

#Commit to save changes in database
conn.commit()

#To close database connection
conn.close()