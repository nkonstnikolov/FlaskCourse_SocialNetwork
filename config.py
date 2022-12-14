from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from db import db
from resources.routes import routes

class ProdConfig:
    FLASK_ENV = "prod"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class DevConfig:
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class TestingConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_HOST')}:{config('DB_PORT')}/{config('TEST_DB_NAME')}"
    )


def create_app(config="config.DevConfig"):
    app = Flask(__name__)
    configuration = config
    app.config.from_object(configuration)
    db.init_app(app)
    api = Api(app)
    migrate = Migrate(app, db)
    CORS(app)
    [api.add_resource(*route) for route in routes]

    return app