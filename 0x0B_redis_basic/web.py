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
    def calback(link):
        """calback func"""
        redis_object.incr("count:{}".format(link))
        c = redis_object.get("cached:{}".format(link))
        if c:
            return c.decode()
        f = method(link)
        redis_object.setex("cached:{}".format(link), 10, f)
        return f

    return calback


@count_req
def get_page(url: str) -> str:
    """get_page"""
    request = requests.get(url)
    return request.text
