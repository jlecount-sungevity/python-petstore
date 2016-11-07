import logging.config

import socket
from logging import Formatter, FileHandler

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from ps import settings
from ps.api.restplus import api

app = Flask(__name__)
db = SQLAlchemy()

def configure_logging(log_level):
    LOGGER = logging.getLogger('whatever')
    handler = logging.StreamHandler()
    handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        )
    )
    LOGGER.addHandler(handler)
    LOGGER.setLevel(log_level)

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_logging(logging.INFO)
    configure_app(flask_app)

    blueprint = Blueprint('/', __name__, url_prefix='/api')
    api.init_app(blueprint)
    from ps.api.petstore.endpoints.users import ns as users_namespace
    from ps.api.petstore.endpoints.auth import ns as auth_namespace
    from ps.api.petstore.endpoints.pet import ns as pet_namespace
    from ps.api.petstore.endpoints.store import ns as store_namespace
    api.add_namespace(users_namespace)
    api.add_namespace(auth_namespace)
    api.add_namespace(pet_namespace)
    api.add_namespace(store_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    flask_app


def main(port):
    initialize_app(app)
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
      port = 5000
    else:
      port = int(sys.argv[1])
    main(port)
