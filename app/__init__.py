from flask import Flask # Import the Flask class from the flask module
from flask_sqlalchemy import SQLAlchemy
from config import Config



# Create an instance of Flask called app which will be the central object
app = Flask(__name__)
#set the configuration for the app
app.config.from_object(Config)

# create an instance of SQLAlchemy called db which will be the central object for our dtabase
db = SQLAlchemy(app)

# import the routes to the app
from . import routes 