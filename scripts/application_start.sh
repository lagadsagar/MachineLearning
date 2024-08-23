#!/bin/bash
# Start the Flask application
source /home/ubuntu/myapp/venv/bin/activate
export FLASK_APP=/home/ubuntu/myapp/app.py
export FLASK_ENV=production
nohup flask run --host=0.0.0.0 --port=80 > /home/ubuntu/myapp/app.log 2>&1 &
