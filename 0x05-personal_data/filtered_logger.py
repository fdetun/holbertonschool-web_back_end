#!/usr/bin/env python3
"""regex"""
import re
from typing import List


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
