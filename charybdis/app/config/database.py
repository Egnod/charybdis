import os

from .base import BaseConfig
from .credentials import get_credential


class DataBaseConfig:
    DB_USER = get_credential("db_user", "charybdis")
    DB_PORT = get_credential("db_port", "5432")
    DB_NAME = get_credential("db_user", "charybdis")
    DB_PASSWORD = get_credential("db_password", "charybdis_secrets")
    DB_HOST = get_credential("db_host", "localhost")

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MIGRATIONS_DIR = os.path.join(BaseConfig.APP_DIR, "migrations/")
