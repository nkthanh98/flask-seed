# coding=utf-8
"""
Logging extension
"""

import os
import traceback as tb
import logging.config
from logging import Formatter as BaseFormatter


class Formatter(BaseFormatter):
    """Formatter
    Format exception logging follow
    [lineno] [filename]
             [line]
    """
    def formatException(self, exc_info): # pylint:disable=W0221
        result = ''
        for item in tb.extract_tb(exc_info[2]):
            result = f'{item.lineno:<6} {item.filename:} \n\t{item.line}\n{result}'
        return result


def init_app(app):
    """init_app

    :param app:
    """
    logging.config.fileConfig(
        fname=os.path.join(app.config['ROOT_DIR'], 'app', 'logging.ini'),
        defaults={'logfile': app.config['LOG_FILE']},
    )
