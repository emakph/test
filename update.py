import sqlite3
#Database connection
conn = sqlite3.connect('students.db')

#Cursor object to execute database query
c = conn.cursor()

ctr = 1
for rows in c.execute('SELECT name FROM tblstudent'):
    for row in rows:
        print(f'{ctr}. {row}')
    ctr +=1


choice = input('Enter name you want to update: ')
name = input('Enter your name: ')

query = 'UPDATE tblstudent SET name=? WHERE name=?'
c.execute(query, (name, choice))

conn.commit()

conn.close()