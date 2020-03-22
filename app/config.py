# coding=utf-8

import os


class BaseConfig:
    ROOT_DIR = os.getcwd()

    LOG_FILE = os.getenv('LOG_FILE', os.path.join('app.log'))

    CPROF_DIR = os.getenv('CPROF_DIR', os.path.join('cprof'))

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    TESTING = False

    DB_HOST = os.getenv('DB_HOST', '127.0.0.1')

    DB_PORT = os.getenv('DB_PORT', 3306)

    DB_USER = os.getenv('DB_USER', 'root')

    DB_PASS = os.getenv('DB_PASS', 'password')

    DB_NAME = os.getenv('DB_NAME', 'app')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class TestingConfig(BaseConfig):
    DEBUG = False

    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(BaseConfig):
    DEBUG = False

    TESTING = False

    DB_HOST = os.getenv('DB_HOST', '127.0.0.1')

    DB_PORT = os.getenv('DB_PORT', 3306)

    DB_USER = os.getenv('DB_USER', 'root')

    DB_PASS = os.getenv('DB_PASS', 'password')

    DB_NAME = os.getenv('DB_NAME', 'app')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


def get_config(name):
    """get_config

    :param name:
    """
    return dict(
        development=DevelopmentConfig,
        testing=TestingConfig,
        production=ProductionConfig
    )[name]
