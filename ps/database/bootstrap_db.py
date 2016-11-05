# coding: utf-8
import sqlite3

con = sqlite3.connect("../db.sqlite")
con.execute("DROP TABLE IF EXISTS quotes")
con.execute("CREATE TABLE quotes(id INTEGER PRIMARY KEY, text char(120) NOT NULL)");

quotes = [q.strip().replace('"','') for q in open('quotes.txt', 'r').readlines()]

# QUOTES
#
for q in quotes:
    con.execute("INSERT into quotes(text) values (?)", (q.decode('utf-8'),))
con.commit()


# TOKENS
#
con.execute("DROP TABLE IF EXISTS token")
con.execute("CREATE TABLE token(id INTEGER PRIMARY KEY, uid INTEGER, value char(40) NOT NULL, is_admin INTEGER NOT NULL, FOREIGN KEY(uid) REFERENCES user(id))")

# USERS
#
con.execute("DROP TABLE IF EXISTS user")
con.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, "
            "role char(100) NOT NULL,"
            "username char(100) NOT NULL, "
            "password char(100) NOT NULL, "
            "bank_account_balance_dollars INTEGER, "
            "status char(100) NOT NULL)")

# PET
#
con.execute("DROP TABLE IF EXISTS pet_status")
con.execute("DROP TABLE IF EXISTS user_status")

con.execute("DROP TABLE IF EXISTS pet")
con.execute("CREATE TABLE pet( id INTEGER PRIMARY KEY, name char(100) NOT NULL, added_at DATETIME, last_modified_by INTEGER, pet_type char(100) NOT NULL, pet_status char(100) NOT NULL, cost INTEGER, FOREIGN KEY(last_modified_by) REFERENCES user(id))")
con.execute("INSERT into pet(name, pet_type, pet_status, cost) values ('Fluffy', 'Cat', 'for sale', 20)")
con.execute("INSERT into pet(name, pet_type, pet_status, cost) values ('Fido', 'Dog', 'for sale', 25)")
con.execute("INSERT into pet(name, pet_type, pet_status, cost) values ('Snaggletooth The Biter', 'Dog', 'for sale', 2)")


con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "jlecount@sungevity.com", "somepass", 0, "non_customer"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "gsandhu@sungevity.com", "sungevity", 0, "non_customer"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "mbrewer@sungevity.com", "somepass", 0, "non_customer"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "kgavar@sungevity.com", "somepass", 0, "non_customer"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "bgordon@sungevity.com", "somepass", 0, "non_customer"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "hkhan@sungevity.com", "sungevity", 0, "non_customer"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "efattig@sungevity.com", "sungevity", 0, "non_customer"));

con.commit()
