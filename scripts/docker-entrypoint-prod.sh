#!/bin/bash

# Collect static files
sleep 10
echo "======= start project ======="

cd /climb-app

python manage.py migrate

echo "======= rm sock ======="
rm climb.sock

echo "======= start gunicorn ======="
gunicorn climb.wsgi:application --workers 4 --preload --bind unix:/climb-app/climb.sock
echo "======= done gunicorn ======="

