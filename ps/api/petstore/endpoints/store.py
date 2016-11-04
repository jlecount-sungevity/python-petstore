import logging

from flask import request
from flask_restplus import Resource
from ps.api.petstore.serializers import category, category_with_posts
from ps.api.restplus import api
from ps.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('store', description='The Pet Emporium')

@api.response(404, 'User not found.')
@ns.route('/')
class Store(Resource):

    @api.marshal_with(order)
    def post(self):
        """
        Returns a user
        """
        if not id:
            users = models.User.query.all()
            print "length of users: {0}".format(len(users))
            if users:
                return users, 200
            else:
                return [], 200
        else:
            return models.User.query.filter(models.User.id == id).one()


    @api.expect(user)
    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={403: 'Not Authorized'})
    @api.response(204, 'User successfully updated.')
    @api.doc(params={'id': 'The userid'})
    def put(self, id):
        """
        Updates a user.
        """
        _authenticate(request)
        data = request.json


        update_user(id, data)
        return None, 204

    @api.expect(userfields_for_creation)
    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={403: 'Not Authorized'})
    @api.response(204, 'Customer user successfully created.')
    def post(self):
        """
        Updates a user.
        """
        _authenticate(request)
        data = request.json


        create_user(data)
        return None, 204

    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={403: 'Not Authorized'})
    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes a user.
        """
        _authenticate(request)
        delete_user(id)
        return None, 204
