# coding=utf-8

import traceback as tb
from logging import Formatter as BaseFormatter


class Formatter(BaseFormatter):
    def formatException(self, exc_info):
        result = ''
        for item in tb.extract_tb(exc_info[2]):
            result = f'{item.lineno:<6} {item.filename:} \n\t{item.line}\n{result}'
        return result
