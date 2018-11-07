import sqlite3
connection = sqlite3.connect('users.db')
c = connection.cursor()
c.execute('SELECT score FROM user')
for i in c.fetchall():
    for j in i:
        print(j)
connection.commit()

