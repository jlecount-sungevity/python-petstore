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


# USER_STATUS
#
con.execute("DROP TABLE IF EXISTS user_status")
con.execute("CREATE TABLE user_status(id INTEGER PRIMARY KEY, status char(100) NOT NULL)")

# PET_STATUS
#
con.execute("DROP TABLE IF EXISTS pet_status")
con.execute("CREATE TABLE pet_status(id INTEGER PRIMARY KEY, status char(100) NOT NULL)")

# TOKENS
#
con.execute("DROP TABLE IF EXISTS token")
con.execute("CREATE TABLE token(id INTEGER PRIMARY KEY, uid INTEGER, value char(40) NOT NULL, is_admin INTEGER NOT NULL, FOREIGN KEY(uid) REFERENCES user(id))")
# PET
#
con.execute("DROP TABLE IF EXISTS pet")
con.execute("CREATE TABLE pet(\
        id INTEGER PRIMARY KEY, \
        name char(100) NOT NULL, \
        added_at DATETIME, \
        added_by INTEGER,\
        type char(100) NOT NULL, \
        status INTEGER, \
        cost INTEGER, \
        FOREIGN KEY(status) REFERENCES pet_status(id), \
        FOREIGN KEY(added_by) REFERENCES user(id))")

# USERS
#
con.execute("DROP TABLE IF EXISTS user")
con.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, "
            "role char(100) NOT NULL,"
            "email char(100) NOT NULL, "
            "password char(100) NOT NULL, "
            "bank_account_balance_dollars INTEGER, "
            "status INTEGER, "
            "FOREIGN KEY(status) REFERENCES user_status(id))")

con.execute("INSERT into user_status(id, status) values (?, ?)", (1, 'registered',))
con.execute("INSERT into user_status(id, status) values (?, ?)", (2, 'unregistered',))

con.execute("INSERT into pet_status(id, status) values (?, ?)", (1, 'sold',))
con.execute("INSERT into pet_status(id, status) values (?, ?)", (2, 'for sale',))
con.execute("INSERT into pet_status(id, status) values (?, ?)", (3, 'removed',))

con.execute("INSERT into user(role, email, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "jlecount@sungevity.com", "somepass", 0, "1"));
con.execute("INSERT into user(role, email, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "gsandhu@sungevity.com", "sungevity", 0, "1"));
con.execute("INSERT into user(role, email, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "mbrewer@sungevity.com", "somepass", 0, "1"));
con.execute("INSERT into user(role, email, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "kgavar@sungevity.com", "somepass", 0, "1"));
con.execute("INSERT into user(role, email, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "bgordon@sungevity.com", "somepass", 0, "1"));
con.execute("INSERT into user(role, email, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "hkhan@sungevity.com", "sungevity", 0, "1"));
con.execute("INSERT into user(role, email, password, bank_account_balance_dollars, status) values (?, ?, ?, ?, ?)",  ("admin", "efattig@sungevity.com", "sungevity", 0, "1"));

con.commit()
