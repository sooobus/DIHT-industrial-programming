#!/bin/bash

echo Starting Unicorn
exec gunicorn todo.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
