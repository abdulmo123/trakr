#!/bin/bash

# Create venv if doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Upgrade pip (optional but good)
# pip install --upgrade pip

# Install app dependencies
pip install -r requirements.txt

# Run app
echo "Starting Flask app..."
python app.py