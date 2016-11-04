from flask_restplus import reqparse

from ps.api.restplus import api

auth_parser = api.parser()
auth_parser.add_argument('username', type=str, required=True, help='the username (typically an email address', location='form')
auth_parser.add_argument('password', type=str, required=True, help='the password', location='form')
auth_parser.add_argument('client_id', type=str, required=True, help='the client_id ', location='form')
auth_parser.add_argument('grant_type', type=str, required=True, help='the grant type. Must be "password"', location='form')
