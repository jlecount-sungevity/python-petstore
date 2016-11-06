import logging
from datetime import time

from api.petstore.business import add_order, delete_order, get_orders
from api.petstore.endpoints.users import _authenticate
from app import db
from flask import abort
from flask import request
from flask_restplus import Resource
from ps.api.petstore.serializers import order, neworder
from ps.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('store', description='The Pet Emporium')

@ns.route('/')
class NewOrderOrListStore(Resource):

    @api.response(200, 'OK')
    @api.marshal_with(order, as_list=True)
    @api.header('Authorization', 'Authorization', required=True)
    def get(self):
        """
        Lists all orders
        """
        _authenticate(request, must_be_admin=True)
        return get_orders()


    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={
        403: 'Not Authorized',
        404: 'No such user or pet',
        422: 'Insufficient funds to purchase',
        201: 'Order created.'
    })
    @api.expect(neworder)
    def post(self):
        """
        Creates a new order
        """
        auth_type = _authenticate(request)
        data = request.json

        order = add_order(data['user_id'], data['pet_id'])
        return order, 201

    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={
        403: 'Not Authorized',
        204: 'Order Deleted'
    })
    def delete(self, id):
        """
        Deletes a user.
        """
        _authenticate(request)
        delete_order(id)
        return None, 204
