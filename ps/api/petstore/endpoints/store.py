import logging

from flask import request
from flask_restplus import Resource
from ps.api.petstore.serializers import category, category_with_posts
from ps.api.restplus import api
from ps.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('api/store', description='Operations related to the '
                                            'petstore')

