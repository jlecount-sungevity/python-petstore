#!/bin/bash

source /usr/local/bin/virtualenvwrapper.sh
#mkvirtualenv --python=/usr/local/bin/python petstore >/dev/null 2>&1 || true
workon petstore
pip install -r requirements.txt
add2virtualenv .
python ps/app.py


