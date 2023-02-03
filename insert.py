import sqlite3

#Database connection
conn = sqlite3.connect('students.db')

#Cursor object to execute database query
c = conn.cursor()

#Getting user input
name = input('Enter your name: ')
age = int(input('Enter your age: '))

#Database query to insert into table
query = 'INSERT INTO tblstudent (name, age) VALUES (?, ?)'
c.execute(query, (name, age))

#Commit to save changes in database
conn.commit()

#To close database connection
conn.close()