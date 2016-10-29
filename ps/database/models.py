from ps.database import db


class PhotoURL(db.Model):
    __tablename__ = 'photo_url'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    parent_id = db.Column(db.Integer, db.ForeignKey('pet.id'))


class PetTag(db.Model):
    __tablename__ = 'pet_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey('pet.id'))


class PetStatus(db.Model):
    # can be available, pending, sold
    __tablename__ = 'pet_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey('pet.id'))


class OrderStatus(db.Model):
    # can be placed, approved, done
    __tablename__ = 'order_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey('order.id'))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Quote(db.Model):
    __tablename__ = 'quotes'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))


class UserStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #parent = db.Column(db.Integer, db.ForeignKey('user'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    status = db.relationship("UserStatus", uselist=False)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    category = db.Column(db.ForeignKey('category.id'))
    type = db.Column(db.String(50))
    photo_urls = db.relationship("PhotoURL")
    pet_status = db.relationship("PetStatus", uselist=False)
    description = db.Column(db.String(1024))
    tags = db.relationship("PetTag")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Pet: {0} ({1})'.format(self.name, self.type)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet = db.Column(db.ForeignKey('pet.id'))
    status = db.Column(db.ForeignKey('order_status.id'))
    is_complete = db.Column(db.Boolean, default=False)


__all__ = [PhotoURL, PetTag, PetStatus,
           Pet, User, UserStatus,
           Category, OrderStatus, PetStatus]
