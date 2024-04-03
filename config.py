import os

from sqlalchemy.engine.url import URL

BASE_DIR = os.path.join(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('DEBUG')


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DEBUG = True
    url_object = URL.create(
        drivername='postgresql+psycopg2',
        username=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PWD'),
        host=os.getenv('DATABASE_HOST'),
        port=os.getenv('DATABASE_PORT'),
        database=os.getenv('DATABASE_NAME')
    )
    SQLALCHEMY_DATABASE_URI = url_object


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    FLASK_DEBUG = False