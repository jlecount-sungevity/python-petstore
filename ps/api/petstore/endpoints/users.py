import logging
import random
import traceback

import flask
from flask_restplus import abort
from flask import request
from flask_restplus import Resource
from ps.api.petstore.business import update_user, delete_user, create_user
from ps.api.petstore.serializers import user, userfields_for_creation
from ps.api.restplus import api
from ps.database import models

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Customer and admin user management '
                                        'API')

def _authenticate(request):
    auth = request.headers.get("Authorization")
    if not auth:
        abort(403, "Required auth token")

    if not auth.startswith("Bearer"):
        abort(403, "Token must be an Authorization: Bearer token!")
    else:
        lastpart = auth.split(" ")[-1]
        if len(lastpart) != 40:
            abort(403, "Invalid auth token")


@ns.route('/')
@api.response(404, 'User not found.')
class ListUserOrCreateNew(Resource):

    @api.marshal_with(user, as_list=True)
    def get(self):
        """
        Lists all users
        """
        users = models.User.query.all()
        if users:
           return users, 200
        else:
            return [], 200


    @api.expect(userfields_for_creation)
    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={403: 'Not Authorized'})
    @api.response(204, 'Customer user successfully created.')
    def post(self):
        """
        Creates a user.
        """
        _authenticate(request)
        data = request.json

        create_user(data)
        return None, 204

@api.response(404, 'User not found.')
@ns.route('/<int:id>')
class User(Resource):

    @api.marshal_with(user)
    def get(self, id):
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


    @api.expect(userfields_for_creation)
    @api.header('Authorization', 'Authorization', required=True)
    @api.response(204, 'User successfully updated.')
    def put(self, id):
        """
        Updates a user.
        """
        _authenticate(request)
        data = request.json


        update_user(id, data)
        return None, 204


    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={
        403: 'Not Authorized',
        204: 'User successfully deleted.',
        400: 'No such user.',
        422: 'Cannot delete user.',
    })
    def delete(self, id):
        """
        Deletes a user.
        """
        _authenticate(request)
        try:
            u = models.User.query.filter(models.User.id == id).one()
            if u.role == 'admin':
                abort(422)
        except: # missing user
            traceback.print_exc()
            abort(400, 'No such user')

        delete_user(id)
        return None, 204
