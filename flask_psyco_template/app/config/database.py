import os

from .config import get_config
from .credentials import get_credential

DB_USER = get_credential("db_user", "db_user")
DB_PORT = get_credential("db_port", "5432")
DB_NAME = get_credential("db_user", "db_name")
DB_PASSWORD = get_credential("db_password", "db_password")
DB_HOST = get_credential("db_host", "db_host")

SQLALCHEMY_DATABASE_URI = f"psycopg2+postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLACLHEMY_TRACK_MODIFICATIONS = False
