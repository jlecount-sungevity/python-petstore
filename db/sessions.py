import sqlite3

from db import dbfunctions

dbfunctions.dbsetup()

con = sqlite3.connect(dbfunctions.DB_FILE)

con.execute("CREATE TABLE sessions (id INTEGER PRIMARY KEY, userid INTEGER NOT NULL, session_id char(100) NOT NULL)")
con.commit()
