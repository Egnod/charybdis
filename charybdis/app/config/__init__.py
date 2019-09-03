from .logging import *
from .base import *
from .database import *


class Config(BaseConfig, LoggingConfig, DataBaseConfig):
    pass
