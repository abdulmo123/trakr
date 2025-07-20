#!/bin/bash

# Create venv if doesn't exist
# if [ ! -d "venv" ]; then
#     python3 -m venv venv
# fi

# Activate venv
# source venv/bin/activate

# Install app deps
pip install -r requirements.txt

# Run app
export FLASK_APP=app.py
# export FLASK_ENV=development
flask run