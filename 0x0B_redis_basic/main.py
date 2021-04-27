#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache
c2 = __import__('exercise')
print(c2.__doc__)
print(Cache.__doc__)

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
