from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from petstore.database.models import *
    db.drop_all()
    db.create_all()
