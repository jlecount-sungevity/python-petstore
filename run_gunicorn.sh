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
mkdir .log 2> /dev/null
pkill -9 gunicocrn
#nohup gunicorn -k gevent --log-level debug --access-logfile /var/tmp/gunicorn/access.log --error-logfile /var/tmp/gunicorn/error.log --worker-connections 10 ps.app:app &
nohup gunicorn --log-level debug --access-logfile /var/tmp/gunicorn/access.log --error-logfile /var/tmp/gunicorn/error.log --workers 10 ps.app:app &
sleep 5
sudo nginx -s reload 


