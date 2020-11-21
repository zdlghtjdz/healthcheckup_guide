import sqlite3

conn = sqlite3.connect("user.db")

conn.execute('CREATE TABLE user_data(time TEXT, age INTEGER, gender TEXT)')

conn.close()

