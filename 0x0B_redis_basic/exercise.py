#!/usr/bin/env python3
"""backend redis project"""
import redis
import uuid
from typing import Union


class Cache:
    """cash class"""

    def __init__(self):
        """initilisation funct"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """store cache methode"""
        tmp = str(uuid.uuid4())
        self._redis.mset({tmp: data})
        return tmp
