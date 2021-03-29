#!/usr/bin/env python3
"""regex"""
import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.f = fields

    def format(self, record: logging.LogRecord) -> str:
        """format the record"""
        form = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.f, self.REDACTION, form, self.SEPARATOR)


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """delim func"""
    for i in fields:
        search = i + "=" + ".*?" + separator
        replace = i + "=" + redaction + separator
        message = re.sub(search, replace, message)
    return message


def get_logger() -> logging.Logger:
    """get logger function"""
    obj = logging.getLogger('user_data')
    obj.propagate = False
    ch = logging.StreamHandler(RedactingFormatter(list(PII_FIELDS)))
    obj.addHandler(ch)
    return obj
