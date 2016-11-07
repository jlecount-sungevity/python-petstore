#!/bin/bash -x

mkdir .log 2> /dev/null
python ps/app.py 5000 &
#python ps/app.py 5001 &
#python ps/app.py 5002 &
#python ps/app.py 5003 &
#python ps/app.py 5004 &
#python ps/app.py 5005 &
sleep 5
sudo nginx -s reload 


