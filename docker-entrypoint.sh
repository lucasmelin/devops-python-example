#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start the huey task service
echo "Starting task queue"
python manage.py run_huey

# Start server
echo "Starting server"
gunicorn -b :8080 lucasmelin_research.wsgi