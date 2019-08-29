from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db, directory=Config.MIGRATIONS_DIR)

    return app

