import os


class BaseConfig(object):
    APP_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
