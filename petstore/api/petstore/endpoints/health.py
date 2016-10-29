import logging
import random

from flask import request
from flask_restplus import Resource
from petstore.api.blog.business import create_blog_post, update_post, delete_post
from petstore.api.blog.serializers import blog_post, page_of_blog_posts
from petstore.api.blog.parsers import pagination_arguments
from petstore.api.restplus import api
from petstore.database.models import Quote

log = logging.getLogger(__name__)

ns = api.namespace('/', description='Health status check')


@ns.route('/')
class HealthStatus(Resource):

    def get(self):
        """
        Returns a random quote as json
        """
        quote = random.choice(Quote.query.all())
        return quote.text


