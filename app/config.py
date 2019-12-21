# coding=utf-8

import os


class BaseConfig:
    ROOT_DIR = os.getcwd()

    LOG_FILE = os.getenv('LOG_FILE', os.path.join('/tmp', 'app.log'))

    CPROF_DIR = os.getenv('CPROF_DIR', os.path.join('/tmp', 'cprof'))

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class TestingConfig(BaseConfig):
    DEBUG = False

    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


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
