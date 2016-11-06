from ps.app import db


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(40))
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_admin = db.Column(db.Integer)

    def is_admin_user(self):
        return self.is_admin == 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100))
    username = db.Column(db.String(100))
    bank_account_balance_dollars = db.Column(db.Integer, default=200)
    password = db.Column(db.String(100))
    customer_status = db.Column(db.String(100))

    def to_json(self):
        return dict(
            id=self.id,
            username = self.username,
            role = self.role,
            bank_account_balance_dollars = self.bank_account_balance_dollars,
            customer_status=self.customer_status
        )


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_modified_by = db.Column(db.ForeignKey('user.id'))
    added_at = db.Column(db.DateTime)
    pet_type = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    pet_status = db.Column(db.String(100))

    def to_json(self):
        return dict(
            id=self.id,
            name= self.name,
            last_modified_by = self.last_modified_by,
            added_at = str(self.added_at),
            pet_type = self.pet_type,
            cost = self.cost,
            pet_status = self.pet_status
        )

    def __repr__(self):
        return 'Pet: {0} ({1})'.format(self.name, self.pet_type)


class Order(db.Model):
    __tablename__ = 'store_order'
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.ForeignKey('pet.id'))
    user_id = db.Column(db.ForeignKey('user.id'))
    status = db.Column(db.String(100)) # completed | deleted
    is_complete = db.Column(db.Boolean, default=True)

    def to_json(self):
        return dict(
            id=self.id,
            pet_id=self.pet_id,
            user_id=self.user_id,
            status=self.status,
            is_complete=self.is_complete
        )
