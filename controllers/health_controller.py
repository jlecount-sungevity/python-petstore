from flask import jsonify

from db import dbfunctions


def get_status():
    rv = dbfunctions.query("select text from expressions order by random() "
                           "limit 1")
    return jsonify(salutation=rv[0][0])
