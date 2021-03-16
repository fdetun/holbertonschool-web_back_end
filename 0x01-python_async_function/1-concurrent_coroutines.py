#!/usr/bin/env python3
""" task1 """

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    """ function basic async"""
    arr = []
    rslt = []
    for i in range(n):
        arr.append(asyncio.create_task(wait_random(max_delay)))
    for j in asyncio.as_completed(arr):
        rslt.append(await j)
    return rslt
