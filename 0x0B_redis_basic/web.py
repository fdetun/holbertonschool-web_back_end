#!/usr/bin/env python3
"""web file"""
from typing import Callable
import requests
import redis
from functools import wraps

redis_object = redis.Redis()


def ctr(method: Callable) -> Callable:
    """req trakker"""

    @wraps(method)
    def calback(url):
        """calback func"""
        redis_object.incr("count:{}".format(url))
        c = redis_object.get("cached:{}".format(url))
        if c:
            return c.decode()
        html = method(url)
        redis_object.setex("cached:{}".format(url), 10, html)
        return html

    return calback


@count_req
def get_page(url: str) -> str:
    """get page"""
    req = requests.get(url)
    return req.text
