# coding: utf-8
import sqlite3

con = sqlite3.connect("../db.sqlite")
con.execute("DROP TABLE quotes")
con.execute("CREATE TABLE quotes(id INTEGER PRIMARY KEY, text char(120) NOT NULL)");

quotes = [q.strip().replace('"','') for q in open('quotes.txt', 'r').readlines()]

# QUOTES
#
for q in quotes:
    con.execute("INSERT into quotes(text) values (?)", (q.decode('utf-8'),))
con.commit()


# USER_STATUS
#
con.execute("DROP TABLE user_status")
con.execute("CREATE TABLE user_status(id INTEGER PRIMARY KEY, status char(100) NOT NULL)")

# USERS
#
con.execute("DROP TABLE user")
con.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username char(100) NOT NULL, first_name char(100) NOT NULL, last_name char(100) NOT NULL, email char(100) NOT NULL, password char(100) NOT NULL, phone char(100) NOT NULL, status INTEGER, FOREIGN KEY(status) REFERENCES user_status(id))")

con.execute("INSERT into user_status(id, status) values (?, ?)", (1, 'alive',))

con.execute("INSERT into user(username, first_name, last_name, email, password, phone, status) values (?, ?, ?, ?, ?, ?, ?)",  \
        ("jlecount", "Jason", "LeCount", "jlecount@sungevity.com", "somepass", "888-867-5309", "1"));

con.commit()
