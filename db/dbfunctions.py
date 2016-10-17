import os

DB_DIR='/var/db/petstore'
DB_FILE = os.pathsep.join([DB_DIR, 'petstore.db'])

def dbsetup():
    try:
        os.mkdirs(DB_DIR)
    except:
        pass