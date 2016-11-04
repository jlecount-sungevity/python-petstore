#!/bin/bash

source $(which virtualenvwrapper.sh)

#mkvirtualenv --python=/usr/local/bin/python petstore >/dev/null 2>&1 || true
. ./set_env.sh
if [ $? -ne 0 ]
then
  echo "errors, gotta exit."
  exit 1
fi
workon petstore
add2virtualenv .
gunicorn -k gevent --bind  0.0.0.0:8080 --log-level debug --access-logfile /var/tmp/gunicorn/access.log --error-logfile /var/tmp/gunicorn/error.log --worker-connections 100 ps.app:app


