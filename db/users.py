import sqlite3

from db import dbfunctions

dbfunctions.dbsetup()

con = sqlite3.connect(dbfunctions.DB_FILE)

con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username char(100) NOT NULL, password char(100) NOT NULL)")
con.execute("INSERT INTO users (username, password) VALUES ('jlecount', 'somepass')")
con.commit()
