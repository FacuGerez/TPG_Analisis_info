#!/bin/bash

# Install the requirements
pip install -r requirements.txt

# Run the FastAPI application
cd App
uvicorn main:app --reload 
