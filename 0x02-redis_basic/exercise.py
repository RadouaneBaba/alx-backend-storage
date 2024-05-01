#!/usr/bin/env python3
""" Cache class implementation """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count how many times method is called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ increment count """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ add inputs and outputs """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ add inputs and outputs """
        key_input = method.__qualname__ + ":inputs"
        key_output = method.__qualname__ + ":outputs"
        self._redis.rpush(key_input, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(key_output, result)
        return result
    return wrapper


class Cache:
    """ Cache redis class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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


def replay(method: Callable):
    """ display history of calls of method """
    storage = redis.Redis()
    n_calls = int(storage.get(method.__qualname__))
    print(f"{method.__qualname__} was called {n_calls} times:")
    inputs = storage.lrange("{}:inputs".format(method.__qualname__), 0, -1)
    outputs = storage.lrange("{}:outputs".format(method.__qualname__), 0, -1)
    for item in zip(inputs, outputs):
        inp = str(item[0], 'utf-8')
        out = str(item[1], 'utf-8')
        print(f"{method.__qualname__}(*{inp}) -> {out}")
