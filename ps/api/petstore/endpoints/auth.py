import logging
import random
import traceback
import user

import flask
from flask import abort
from flask import request
from flask_restplus import Resource
from ps.api.petstore.parsers import auth_parser
from ps.api.restplus import api
from ps.app import db
from ps.database import models
from ps.api.petstore.serializers import user
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

ns = api.namespace('auth/token', description='authentication')


@ns.route('/')
@api.response(403, 'Invalid username or password.')
class Token(Resource):
    def create_token(self):
        alpha = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                 "a", "b", "c", "d", "e", "f")
        return ''.join([random.choice(alpha) for _ in range(40)])

    @api.doc(parsers=auth_parser)
    @api.expect(auth_parser)
    def post(self):
        try:
            # handle either post body or form
            if request.json:
                username = request.json['username']
                password = request.json['password']
                client_id = request.json['client_id']
                grant_type = request.json['grant_type']
            else:
                username = request.form['username']
                password = request.form['password']
                client_id = request.form['client_id']
                grant_type = request.form['grant_type']
        except:
            traceback.print_exc()

        if not client_id:
            abort(403, "missing client_id")

        if not grant_type or grant_type != 'password':
            abort(403, "missing or invalid grant_type")

        tokenvalue = self.create_token()
        role_value = 0
        try:
            u = models.User.query.filter(
                models.User.username == username and
                models.User.password == password
            ).one()
            if u.role == 'admin':
                role_value = 1

        except NoResultFound:
            print "Debug -- no cannot auth, no user: {0} / {1}".format(
                username,
                password
            )
            abort(403, "Invalid username or password")
        except:
            traceback.print_exc()
            abort(500, "Unknown error!")
        output = {
            'token_type':   'Bearer',
            'scope':        'sungevity.com',
            'expires_in':   3600,
            'access_token': tokenvalue
        }
        dbtoken = models.Token(
            value=tokenvalue,
            uid=u.id,
            is_admin=role_value
        )
        models.Token.query.filter(
            models.Token.uid == u.id
        ).delete()
        db.session.add(dbtoken)
        db.session.commit()

        print "output is {0}".format(output)
        return flask.jsonify(output)
