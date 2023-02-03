import sqlite3

#Database connection
conn = sqlite3.connect('ml.db')

#Cursor object to execute database query
c = conn.cursor()

while True:
    menu = input('1. CREATE\n2. INSERT\n3. UPDATE\n4. VIEW\n5. VIEW ALL\n>> ')


    if menu == '':
        break
    elif menu == '1':
        #Database query to create table and columns
        query = 'CREATE TABLE IF NOT EXISTS reymark (skill1 text, skill2 text, skill3 text, skill4 text)'
        c.execute(query)
        conn.commit()

    elif menu == '2':
        #Getting user input
        skill1 = input('Enter your first skill: ')
        skill2 = input('Enter your second skill: ')
        skill3 = input('Enter your third skill: ')
        skill4 = input('Enter your ultimate skill: ')

        #Database query to insert into table
        query = 'INSERT INTO reymark (skill1, skill2, skill3, skill4) VALUES (?, ?, ?, ?)'
        c.execute(query, (skill1, skill2, skill3, skill4))
        conn.commit()

    elif menu == '3':
        update_skill1 = input('Enter your first skill: ')
        update_skill2 = input('Enter your second skill: ')
        update_skill3 = input('Enter your third skill: ')
        update_skill4 = input('Enter your ultimate skill: ')

        query = 'UPDATE reymark SET skill1=?, skill2=?, skill3=? WHERE skill4=?'
        c.execute(query, (update_skill1, update_skill2, update_skill3, update_skill4))

        conn.commit()

    elif menu == '4':
        ultimate_skill = input('Enter ultimate skill: ')

        query = 'SELECT * FROM reymark WHERE skill4=?'
        c.execute(query, (ultimate_skill,))
        print(c.fetchall())
    elif menu == '5':
        query = 'SELECT * FROM reymark'
        for row in c.execute(query):
            print(row)

    else:
        print('INVALID INPUT')

conn.close()