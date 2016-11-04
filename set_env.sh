#!/bin/bash

which virtualenvwrapper.sh
if [ $? -ne 0 ]
then
  echo "You must have virtualenvwrapper.sh in your PATH"
  return 1
else
  source $(which virtualenvwrapper.sh)
fi
workon petstore
if [ $? -ne 0 ]
then
  echo "Recreating petstore virtualenv."
  mkvirtualenv --python=/usr/local/bin/python petstore >/dev/null 2>&1 || true
  workon petstore
fi
which python | grep petstore >/dev/null 2>&1
if [ $? -ne 0 ]
then
  echo "Failed to enter virtualenv!"
  return 1
else
  pip install -r requirements.txt
  add2virtualenv .
fi

