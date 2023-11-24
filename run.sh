#!/bin/bash

# Install python3-venv
sudo apt-get install python3.10-venv

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source ./venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run the FastAPI application
cd App || exit
uvicorn main:app --reload
