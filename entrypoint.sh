#!/bin/sh

#sometimes postgresql server is started too quickly so automatic build fails:
sleep 4

python3 /code/oak/manage.py makemigrations
python3 /code/oak/manage.py migrate
exec "$@"
