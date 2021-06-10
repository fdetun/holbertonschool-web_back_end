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
    def wrapper(url):
        k = "cached:" + url
        cached_data = redis_object.get(k)
        if cached_data:
            return cached_data.decode()
        ck = "count:" + url
        a = method(url)
        redis_object.incr(ck)
        redis_object.set(k, a)
        redis_object.expire(k, 10)
        return a
    return wrapper


@count_req
def get_page(url: str) -> str:
    """get_page"""
    request = requests.get(url)
    return request.text
