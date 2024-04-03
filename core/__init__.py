import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

_ = load_dotenv()

database = SQLAlchemy()
def create_app(config_type=os.getenv('CONFIG_TYPE')):
    app = Flask(__name__)
    app.config.from_object(config_type)
    initialize_app(app)
    return app

def initialize_app(app):
    database.init_app(app)