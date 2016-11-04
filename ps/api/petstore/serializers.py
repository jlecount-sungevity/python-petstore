from flask_restplus import fields
from ps.api.restplus import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'email': fields.String(required=True, description='email'),
    'password': fields.String(required=True, description='password'),
    'role': fields.String(required=True, attribute='role.id'),
    'bank_account_balance_dollars': fields.Integer(required=True, description='email'),
    'status': fields.String(required=True, attribute='user_status.id'),
})

userfields_for_creation = api.model('User', {
    'email': fields.String(required=True, description='email',
                           default="foo@bar.org"),
    'password': fields.String(required=True, description='password',
                              default="my_strong_password"),
    'bank_account_balance_dollars': fields.Integer(required=True,
                                                   description='email',
                                                   default=200),
})

pet = api.model('Pet', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a pet'),
    'added_at': fields.DateTime(readOnly=True, description='The time the pet was added to the db'),
    'added_by': fields.Integer(required=True, attribute='user.id', description="The admin user who added the pet to the db"),
    'name': fields.String(required=True, description='pet name'),
    'type': fields.String(required=True, description='type (dog, cat, etc)'),
    'status': fields.String(required=True, attribute='pet_status.id'),
    'cost': fields.Integer(required=True, description='email')
})

newpet = api.model('Pet', {
    'name': fields.String(required=True, description='pet name'),
    'type': fields.String(required=True, description='type (dog, cat, etc)'),
    'cost': fields.Integer(required=True, description='email')
})

order = api.model('Order', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'pet': fields.Integer(required=True, attribute='pet.id'),
    'status': fields.Integer(required=True, attribute='order_status.id'),
    'is_complete': fields.Boolean(default=False),
    'user': fields.Integer(required=True, attribute='user.id'),
})