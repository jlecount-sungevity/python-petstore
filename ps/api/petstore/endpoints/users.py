import logging
import traceback

import flask
import ps
from flask_restplus import abort
from flask import request
from flask_restplus import Resource
from ps.api.petstore.business import update_user, delete_user, create_user
from ps.api.petstore.serializers import user, userfields_for_creation
from ps.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('users', description='Customer and admin user management API')

def _authenticate(request, must_be_admin=False):
    auth = request.headers.get("Authorization")
    if not auth:
        abort(403, "Required auth token")

    if not auth.startswith("Bearer"):
        abort(403, "Token must be an Authorization: Bearer token!")
    else:
        lastpart = auth.split(" ")[-1]
        if len(lastpart) != 40:
            abort(403, "Invalid auth token")
        token = None
        try:
            token = ps.database.models.Token.query.filter(
                ps.database.models.Token.value == lastpart
            ).one()
        except:
            # BUG, let's let them in anyway as a non-admin user
            return
        if must_be_admin:
            if not token.is_admin:
                abort(403, "Invalid auth token: not admin")



@ns.route('/')
class ListUserOrCreateNew(Resource):

    @api.response(200, 'OK')
    @api.marshal_with(user, as_list=True)
    def get(self):
        """
        Return a list of all users.
        """
        from ps.database import models
        users = models.User.query.all()
        import ipdb; ipdb.set_trace()
        if users:
           return users, 200
        else:
            return [], 200


    @api.expect(userfields_for_creation)
    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={403: 'Not Authorized'})
    @api.response(201, 'Customer user successfully created.')
    def post(self):
        """
        Creates a user.
        """
        _authenticate(request)
        data = request.json

        new_user = create_user(data)
        return new_user, 201

@api.response(404, 'User not found.')
@ns.route('/<int:id>')
class User(Resource):

    @api.marshal_with(user)
    def get(self, id):
        """
        Returns a user
        """
        from ps.database import models
        return models.User.query.filter(models.User.id == id).one()


    @api.expect(userfields_for_creation)
    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(
        responses={
            403: 'Not Authorized',
            204: 'User successfully updated.',
            404: 'No such user.',
            422: 'You may not update admin users.',
        }
    )
    def put(self, id):
        """
        Updates a user.  Only admin users can update users.  Only
        customers may be updated via this API.
        """
        print "authenticate"
        _authenticate(request, must_be_admin=True)
        print "Getting data"
        data = request.json
        print "Got data"


        update_user(id, data)
        return None, 204


    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={
        403: 'Not Authorized',
        204: 'User successfully unregistered.',
        400: 'No such user.',
        422: 'Cannot unregister user.',
    })
    def delete(self, id):
        """
        Deletes a user.  Only admin users can delete users, and other admins
        may not be deleted.
        """
        _authenticate(request, must_be_admin=True)
        u = None
        try:
            from ps.database import models
            u = models.User.query.filter(models.User.id == id).one()
        except: # missing user
            traceback.print_exc()
            abort(400, 'No such user')

        if u.role == 'admin':
            abort(422, "Cannot unregister an admin user")

        delete_user(id)
        return None, 204

