#!/bin/bash

source $(which virtualenvwrapper.sh)

#mkvirtualenv --python=/usr/local/bin/python petstore >/dev/null 2>&1 || true
workon petstore
pip install -r requirements.txt
add2virtualenv .
gunicorn --log-level debug --access-logfile /var/tmp/gunicorn/access.log --error-logfile /var/tmp/gunicorn/error.log --workers=1 ps.app:app


