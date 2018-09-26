import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'marbles', 'jasper')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'mary', 'jasper'),
    (3, 'charlie', 'jasper'),
    (4, 'milo', 'jasper')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users WHERE username=='marbles'"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
