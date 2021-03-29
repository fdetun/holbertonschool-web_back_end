#!/usr/bin/env python3
"""regex"""
import re


def filter_datum(fields, redaction, message, separator):
    """delim func"""
    for i in fields:
        search = i + "=" + ".*?" + separator
        replace = i + "=" + redaction + separator
        message = re.sub(search, replace, message)
    return message
