#!/bin/bash

# Create the main project directory
#mkdir -p mini-app

# Navigate into the main project directory
#cd mini-app

# Create backend directory and files
mkdir -p backend
touch backend/app.py
touch backend/requirements.txt
touch backend/Dockerfile

# Create frontend directory and subdirectories
mkdir -p frontend/public
mkdir -p frontend/src

# Create frontend files
touch frontend/src/App.js
touch frontend/src/index.js
touch frontend/package.json
touch frontend/Dockerfile

# Create project-level files
touch docker-compose.yml
#touch .env

echo "Directory and file structure created successfully!"
