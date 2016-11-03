from flask_restplus import reqparse

from ps.api.restplus import api

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('bool', type=bool, required=False, default=1, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                                  default=10, help='Results per page {error_msg}')

auth_parser = api.parser()
auth_parser.add_argument('username', type=str, required=True, help='the username', location='form')
auth_parser.add_argument('password', type=str, required=True, help='the password', location='form')
auth_parser.add_argument('client_id', type=str, required=True, help='the client_id ', location='form')
auth_parser.add_argument('grant_type', type=str, required=True, help='the grant type. Must be "password"', location='form')
