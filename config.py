import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
FLASK_ENVIRONMENT='development'
# Connect to the database


# DONE TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:4y7sV96vA9wv46VR@192.168.100.10:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
