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
            "customer_status char(100))")


# PET
#
con.execute("DROP TABLE IF EXISTS pet")
con.execute("CREATE TABLE pet( id INTEGER PRIMARY KEY, name char(100) NOT NULL, added_at DATETIME, last_modified_by INTEGER, pet_type char(100) NOT NULL, pet_status char(100) NOT NULL, cost INTEGER, FOREIGN KEY(last_modified_by) REFERENCES user(id))")
con.execute("INSERT into pet(name, pet_type, pet_status, cost) values ('Fluffy', 'Cat', 'for sale', 20)")
con.execute("INSERT into pet(name, pet_type, pet_status, cost) values ('Fido', 'Dog', 'for sale', 25)")
con.execute("INSERT into pet(name, pet_type, pet_status, cost) values ('Snaggletooth The Biter', 'Dog', 'for sale', 2)")


# ORDERS
#
con.execute("DROP TABLE IF EXISTS store_order")
con.execute("CREATE TABLE store_order( id INTEGER PRIMARY KEY AUTOINCREMENT, pet_id INTEGER, user_id INTEGER, status char(100) NOT NULL, is_complete INTEGER NOT NULL, FOREIGN KEY(pet_id) REFERENCES pet(id), FOREIGN KEY(user_id) REFERENCES user(id))")

# ADMIN USERS
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "jlecount@sungevity.com", "7655ab", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "gsandhu@sungevity.com", "434fda8", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "mbrewer@sungevity.com", "343a9", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "kwu@sungevity.com", "af7dakk", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "kgavar@sungevity.com", "432235", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "bgordon@sungevity.com", "adsafl33", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "hkhan@sungevity.com", "9afjjj", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "efattig@sungevity.com", "89adfa", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "jtanner@sungevity.com", "34300jk", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "spolonsky@sungevity.com", "eruagg", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "biamranond@sungevity.com", "pouief", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "manantha@sungevity.com", "aPPPa", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "rvandijk@sungevity.com", "n343y", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "mcalderaz@sungevity.com", "<>43<>", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "shernandez@sungevity.com", "55443HI", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "skutty@sungevity.com", "iafsd34", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "rkaul@sungevity.com", "ytrfg89", 0));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars) values (?, ?, ?, ?)",  ("admin", "sakerson@sungevity.com", "67564a", 0));

# CUSTOMERS
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, customer_status) values (?, ?, ?, ?, ?)",  ("customer", "joebob@bob.com", "strongpass", 10, "registered"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, customer_status) values (?, ?, ?, ?, ?)",  ("customer", "sally@gmail.com", "nobodywillguess", 75, "registered"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, customer_status) values (?, ?, ?, ?, ?)",  ("customer", "dave@example.org", "nobodywillguess", 100, "registered"));
con.execute("INSERT into user(role, username, password, bank_account_balance_dollars, customer_status) values (?, ?, ?, ?, ?)",  ("customer", "fred@yahoo.com", "petlover", 50, "registered"));

con.commit()
