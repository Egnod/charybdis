from .base import *
from .database import *
from .dramatiq import DramatiqConfig
from .logging import *
from .secrets import SecretsConfig


class Config(BaseConfig, LoggingConfig, DataBaseConfig, DramatiqConfig, SecretsConfig):
    pass
