from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dramatiq import Dramatiq
from flask_potion import Api

from .config import Config
from .mixin import IdModel

db = SQLAlchemy(model_class=IdModel)
migrate = Migrate(directory=Config.MIGRATIONS_DIR)
dramatiq = Dramatiq()
api = Api()


from charybdis.app.models import *
from charybdis.app.resources import *


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    dramatiq.init_app(app)
    api.init_app(app)

    return app
