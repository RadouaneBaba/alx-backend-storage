#!/usr/bin/env python3
""" Cache class implementation """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Cache redis class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis db """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """ convert bytes to right type """
        value = self._redis.get(key)
        if not value or not fn:
            return value
        return fn(value)

    def get_str(self, key: str) -> str:
        """ convert bytes to str """
        return self.get(key, lambda x: str(x, 'utf-8'))

    def get_int(self, key: str) -> int:
        """ convert bytes to int """
        return self.get(key, int)
