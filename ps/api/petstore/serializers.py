from flask_restplus import fields
from ps.api.restplus import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password'),
    'role': fields.String(required=True, description="admin or customer"),
    'bank_account_balance_dollars': fields.Integer(required=True, description='username'),
    'customer_status': fields.String(required=True, description="valid values: NONE or registered or deleted")
})

userfields_for_creation = api.model('User', {
    'username': fields.String(required=True, description='username')
    'password': fields.String(required=True, description='password',
                              default="my_strong_password"),
    'bank_account_balance_dollars': fields.Integer(required=True,
                                                   description='username',
                                                   default=200),
})

pet = api.model('Pet', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a pet'),
    'added_at': fields.DateTime(readOnly=True, description='The time the pet was added to the db'),
    'last_modified_by': fields.Integer(required=True, attribute='user.id', description="The admin user who added the pet to the db"),
    'name': fields.String(required=True, description='pet name'),
    'pet_type': fields.String(required=True, description='type (dog, cat, etc)'),
    'pet_status': fields.String(required=True, description="sold or for_sale or removed"),
    'cost': fields.Integer(required=True, description='username')
})

newpet = api.model('Pet', {
    'name': fields.String(required=True, description='pet name', default="Fido"),
    'pet_type': fields.String(required=True, description='type (dog, cat, etc)', default="dog"),
    'cost': fields.Integer(required=True, description='the cost of the pet', default=20)
})

order = api.model('Order', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'pet': fields.Integer(required=True, attribute='pet.id'),
    'status': fields.String(required=True, description="valid values are: completed | deleted"),
    'is_complete': fields.Boolean(default=False),
    'user': fields.Integer(required=True, attribute='user.id'),
})

neworder = api.model('Order', {
    'pet_id': fields.Integer(required=True, attribute='pet.id'),
    'status': fields.String(required=False, description="valid values are completed | deleted", default="completed"),
    'user_id': fields.Integer(required=True, attribute='user.id'),
})
