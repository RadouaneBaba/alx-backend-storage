#!/usr/bin/env python3
""" Cache class implementation """
import redis
import uuid


class Cache:
    """ Cache redis class """
    def __init__(self: object):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self:object, data: object) -> str:
        """ store data in redis db """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
