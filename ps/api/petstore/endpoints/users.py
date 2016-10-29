import logging

from flask import request
from flask_restplus import Resource
from ps.api.petstore.business import create_pet
from ps.api.petstore.serializers import blog_post, page_of_blog_posts
from ps.api.petstore.parsers import pagination_arguments
from ps.api.restplus import api
from ps.database.models import Pet

log = logging.getLogger(__name__)

ns = api.namespace('api/users', description='Operations related to user mgmt')


@ns.route('/')
class PostsCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_blog_posts)
    def get(self):
        """
        Returns list of blog posts.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        posts_query = Post.query
        posts_page = posts_query.paginate(page, per_page, error_out=False)

        return posts_page

    @api.expect(blog_post)
    def post(self):
        """
        Creates a new blog post.
        """
        create_pet(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class User(Resource):

    @api.marshal_with(blog_post)
    def get(self, id):
        """
        Returns a user
        """
        return User.query.filter(User.id == id).one()

    @api.expect(blog_post)
    @api.response(204, 'Post successfully updated.')
    def put(self, id):
        """
        Updates a blog post.
        """
        data = request.json
        update_user(id, data)
        return None, 204

    @api.response(204, 'Post successfully deleted.')
    def delete(self, id):
        """
        Deletes blog post.
        """
        delete_user(id)
        return None, 204

