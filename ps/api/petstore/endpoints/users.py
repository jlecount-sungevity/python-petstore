import logging
import random
import traceback

import flask
from flask import abort
from flask import request
from flask_restplus import Resource
from ps.api.petstore.business import update_user, delete_user
from ps.api.petstore.serializers import user
from ps.api.restplus import api
from ps.database import models

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Operations related to user mgmt')

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
class User(Resource):


    @api.marshal_with(user)
    def get(self, id):
        """
        Returns a user
        """
        return models.User.query.filter(models.User.id == id).one()

    @api.expect(user)
    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={403: 'Not Authorized'})
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
    @api.doc(responses={403: 'Not Authorized'})
    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes a user.
        """
        _authenticate(request)
        delete_user(id)
        return None, 204

