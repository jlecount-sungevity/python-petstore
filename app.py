#!/usr/bin/env python

import connexion
import sys

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/', server='gevent')
    app.add_api('swagger.yaml', arguments={
        'title':
        'This is a sample server Petstore server.  You can find out more about '
        'Swagger at [http://swagger.io](http://swagger.io) or on '
        '[irc.freenode.net, #swagger](http://swagger.io/irc/).  '
        'For this sample, you can use the api key &#x60;special-key&#x60; '
        'to test the authorization filters.'}
    )
    if len(sys.argv) < 2:
        print "You must also pass in the port as the first and only arg!"
        sys.exit(1)
    else:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
