from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from ps.database.models import PhotoURL, PetTag, PetStatus,\
               Pet, User, UserStatus,\
               Category, OrderStatus, PetStatus
    db.drop_all()
    db.create_all()
