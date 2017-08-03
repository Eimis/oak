#!/bin/sh
python3 /code/oak/manage.py makemigrations
python3 /code/oak/manage.py migrate
exec "$@"
