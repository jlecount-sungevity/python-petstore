from flask_restplus import fields
from ps.api.restplus import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'username': fields.String(required=True, description='username'),
    'first_name': fields.String(required=True, description='first name'),
    'last_name': fields.String(required=True, description='last name'),
    'email': fields.String(required=True, description='email'),
    'phone': fields.String(required=True, description='phone'),
    'status': fields.String(required=True, attribute='status.id'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

category = api.model('Blog category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
    'name': fields.String(required=True, description='Category name'),
})
