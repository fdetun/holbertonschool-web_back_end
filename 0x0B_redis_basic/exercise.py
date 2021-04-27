#!/usr/bin/env python3
"""redis backend project exercice"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """ the caching class"""

    def __init__(self):
        """ init of cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store caching"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """get caching"""
        fde = self._redis.get(key)
        return fde if fn is None else fn(fde)
