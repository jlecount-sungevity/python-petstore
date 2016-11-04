import logging.config

import socket
from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from ps import settings
from ps.api.restplus import api

app = Flask(__name__)
db = SQLAlchemy()
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


host='localhost'
port=8888

if 'JLECOUNT' not in socket.gethostname():
    host='0.0.0.0'
    port=80


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('/', __name__, url_prefix='/api')
    api.init_app(blueprint)
    from ps.api.petstore.endpoints.users import ns as users_namespace
    from ps.api.petstore.endpoints.auth import ns as auth_namespace
    from ps.api.petstore.endpoints.pet import ns as pet_namespace
    api.add_namespace(users_namespace)
    api.add_namespace(auth_namespace)
    api.add_namespace(pet_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    flask_app


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG, host=host, port=port)

if __name__ == "__main__":
    main()
