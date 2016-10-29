import logging
import random
import traceback

import flask
from flask_restplus import Resource
from ps.api.restplus import api
from ps.database.models import Quote, db

log = logging.getLogger(__name__)

ns = api.namespace('/', description='Health status check')


@ns.route('/')
class HealthStatus(Resource):

    _quotes = []

    @property
    def quotes(self):
        """
        Quotes are static, so load them all once, then serve from memory.
        :return: a list of quotes
        """
        if not self._quotes:
            self._quotes = Quote.query.all()
        return self._quotes



    def get(self):
        """
        Returns a random quote as json
        """

        try:
            output = {
                'salutation' : random.choice(self.quotes).text
            }
            return flask.jsonify(output)
        except:
            traceback.print_exc()


