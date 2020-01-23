#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn demo_django.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1