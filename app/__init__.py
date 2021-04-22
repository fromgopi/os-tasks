#pylint: disable=import-error, missing-final-newline,trailing-whitespace,import-outside-toplevel
""" main package """
import os

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from app.db.database import Database
# from app.db import initialize_db

APP_ROOT = os.path.join(os.path.dirname(__file__), '..') 
DOTENV_PATH = os.path.join(APP_ROOT, '.env')   

def create_app():
    """Entry point for the Flask app.

    Returns:
        Flask Instance: Returns Flask instance with all preloaded env variables
    """
    app = Flask(__name__)
    load_dotenv(dotenv_path=DOTENV_PATH)
    load_config(app)
    # initialize_db(app=app)
    load_blueprints(app=app)
    # api = Api(app)
    # load_resources(api=api)
    load_db()
    return app

def load_config(app):
    """
    Loads all the config items into flask from .env

    Args:
        app ([Flask]): Flask instance
    """
    app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')
    app.config['APPLICATION_ROOT'] = os.getenv('APP_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['MONGODB_DB'] = os.getenv('MONGODB_DB')
    app.config['MONGODB_HOST'] = os.getenv('MONGODB_HOST')
    app.config['MONGODB_PORT'] = int(os.getenv('MONGODB_PORT'))
    app.config['MONGODB_USERNAME'] = os.getenv('MONGODB_USERNAME')
    app.config['MONGODB_PASSWORD'] = os.getenv('MONGODB_PASSWORD')


def load_resources(api):
    """
    Loads all the routes into flask instance

    Args:
        api : Flask restfull instance
    """
    from app.resources import initialize_routes
    initialize_routes(api)


def load_db():
    """
    loads db
    """
    db = Database()

def load_blueprints(app, URL_PREFIX=os.getenv('ROUTE_PREFIX')):
    """
    Loads all the blueprints into flask instance

    Args:
        app (Flask-App): Flask instance
        URL_PREFIX (Str): URL Prefix
    """
    from app.resources.user.controllers.user import USER_API as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix=URL_PREFIX)
    