from ps.app import db


class PetStatus(db.Model):
    # can be available, pending, sold
    __tablename__ = 'pet_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(40))
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_admin = db.Column(db.Integer)

    def is_admin_user(self):
        return self.is_admin == 1

class OrderStatus(db.Model):
    # can be placed, approved, done
    __tablename__ = 'order_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey('order.id'))


class UserStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    role = db.Column(db.String(100))
    bank_account_balance_dollars = db.Column(db.Integer, default=200)
    password = db.Column(db.String(100))
    status = db.Column(db.ForeignKey('user_status.id'))

    def to_json(self):
        return dict(
            id=self.id,
            username = self.username,
            role = self.role,
            bank_account_balance_dollars = self.bank_account_balance_dollars,
            status=self.status
        )


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    added_by = db.Column(db.ForeignKey('user.id'))
    added_at = db.Column(db.DateTime)
    pet_type = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    pet_status_id = db.Column(db.Integer, db.ForeignKey('pet_status.id'))
    pet_status = db.relationship("PetStatus", uselist=False)

    def __repr__(self):
        return 'Pet: {0} ({1})'.format(self.name, self.pet_type)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet = db.Column(db.ForeignKey('pet.id'))
    user = db.Column(db.ForeignKey('user.id'))
    status = db.Column(db.ForeignKey('order_status.id'))
    is_complete = db.Column(db.Boolean, default=False)


__all__ = [PetStatus, Pet, User, UserStatus,
           OrderStatus, PetStatus]
