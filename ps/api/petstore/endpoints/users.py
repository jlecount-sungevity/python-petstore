import logging
import traceback

from flask import request
from flask_restplus import Resource
from ps.api.petstore.business import update_user, delete_user
from ps.api.petstore.serializers import user
from ps.api.restplus import api
from ps.database import models

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Operations related to user mgmt')


@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class User(Resource):

    @api.marshal_with(user)
    def get(self, id):
        """
        Returns a user
        """
        return models.User.query.filter(models.User.id == id).one()

    @api.expect(user)
    @api.response(204, 'User successfully updated.')
    def put(self, id):
        """
        Updates a user.
        """
        data = request.json
        update_user(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes a user.
        """
        delete_user(id)
        return None, 204

