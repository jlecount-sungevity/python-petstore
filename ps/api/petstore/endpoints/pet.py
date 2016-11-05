import logging

from flask import request
from flask_restplus import Resource
from ps.api.petstore.business import create_pet, delete_pet
from ps.api.petstore.endpoints.users import _authenticate
from ps.api.petstore.serializers import pet, newpet
from ps.api.restplus import api
from ps.database.models import Pet

log = logging.getLogger(__name__)

ns = api.namespace('pets', description='The pet management API')

@ns.route('/')
class ListPetsOrCreateNew(Resource):
    @api.marshal_list_with(pet)
    @api.doc(responses={ 200: 'OK' })
    def get(self):
        """
        Returns list of pets
        """
        pets = Pet.query.all()
        return pets


    @api.header('Authorization', 'Authorization', required=True)
    @api.doc(responses={
        201: 'Created',
        403: 'Not Authorized'}
    )
    @api.expect(newpet)
    def post(self):
        """
        Creates a new pet
        """
        print "Got right method"
        _authenticate(request)
        print "Got past auth"
        data = request.json
        print "read the data, sending to create_pet"
        new_pet = create_pet(data)
        return new_pet, 201

@ns.route('/<int:id>')
class PetById(Resource):


    @api.marshal_with(pet)
    @api.doc(responses={
        200: 'OK',
        404: 'No such pet with id'}
    )
    def get(self, id):
        """
        Returns a pet by id
        """
        return Pet.query.filter(Pet.id == id).one()


    @api.doc(responses={
        204: 'Deleted',
        403: 'You must pass admin user credentials',
        404: 'No such pet with id'
    })
    def delete(self, id):
        """
        Returns a pet by id
        """
        print "About to delete pet with id {0}".format(id)
        delete_pet(id)
        return 204, None



