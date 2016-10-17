import os

import sqlite3
from contextlib import contextmanager

DB_DIR = os.path.join(os.getenv("HOME"), 'petstore')
DB_FILE = os.path.join(DB_DIR, 'petstore.db')

def query(q):
    conn = sqlite3.connect(DB_FILE)
    rv = conn.execute(q).fetchall()
    conn.close()
    return rv

def dbsetup():
    try:
        os.mkdirs(DB_DIR)
    except:
        pass
