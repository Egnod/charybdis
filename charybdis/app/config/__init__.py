from .logging import *
from .base import *
from .database import *
from .dramatiq import DramatiqConfig


class Config(BaseConfig, LoggingConfig, DataBaseConfig, DramatiqConfig):
    pass
