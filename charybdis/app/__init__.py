from flask import Flask
from flask_dramatiq import Dramatiq
from flask_jwt import JWT
from flask_migrate import Migrate
from flask_potion import Api
from flask_sqlalchemy import SQLAlchemy

from .api_alchemy_manager import SQLAlchemyManager
from .config import Config
from .mixin import IdModel

db = SQLAlchemy(model_class=IdModel)
migrate = Migrate(directory=Config.MIGRATIONS_DIR)
dramatiq = Dramatiq()
api = Api(default_manager=SQLAlchemyManager)
jwt = JWT()

from .models import *  # isort:skip
from .resources import *  # isort:skip
from .auth import *  # isort:skip
from ..util import first_start, is_first_start  # isort:skip


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    dramatiq.init_app(app)
    api.init_app(app)
    jwt.init_app(app)

    if is_first_start():
        with app.app_context():
            first_start(db)

    return app
