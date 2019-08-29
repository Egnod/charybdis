import os

from .credentials import get_credential
from .base import BaseConfig


class DataBaseConfig(object):
    DB_USER = get_credential("db_user", "db_user")
    DB_PORT = get_credential("db_port", "5432")
    DB_NAME = get_credential("db_user", "db_name")
    DB_PASSWORD = get_credential("db_password", "db_password")
    DB_HOST = get_credential("db_host", "db_host")

    SQLALCHEMY_DATABASE_URI = f"psycopg2+postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MIGRATIONS_DIR = os.path.join(BaseConfig.APP_DIR, "migrations/")

