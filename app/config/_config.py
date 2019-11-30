# coding=utf-8

import os


class BaseConfig:
    ROOT_DIR = os.getcwd()

    LOG_FILE = os.getenv('LOG_FILE', os.path.join('/tmp', 'app.log'))


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    TESTING = True

class TestingConfig(BaseConfig):
    DEBUG = False

    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False

    TESTING = False


def get_config(name):
    """get_config

    :param name:
    """
    return dict(
        development=DevelopmentConfig,
        testing=TestingConfig,
        production=ProductionConfig
    )[name]
