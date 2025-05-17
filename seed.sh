#!/bin/sh

echo "Running migrations..."
python manage.py migrate

echo "Seeding products..."
python manage.py seed_products

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000