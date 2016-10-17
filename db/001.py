import sqlite3

from . import dbfunctions

dbfunctions.dbsetup()

con = sqlite3.connect(dbfunctions.DB_FILE)

con.execute("CREATE TABLE pets (id INTEGER PRIMARY KEY, name char(100) NOT NULL, "
            "type char(30) NOT NULL)")
con.execute("INSERT INTO pets (name,type) VALUES ('Fluffy', 'dog')")
con.execute("INSERT INTO pets (name,type) VALUES ('Purr', 'cat')")
con.commit()
