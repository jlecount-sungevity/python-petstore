# coding: utf-8
import sqlite3

con = sqlite3.connect("../db.sqlite")
con.execute("CREATE TABLE quotes(id INTEGER PRIMARY KEY, text char(120) NOT NULL)");

quotes = open('quotes.txt', 'r').readlines()

for q in quotes:
    con.execute("INSERT into quotes(text) values (?)", (q.decode('utf-8'),))
con.commit()
