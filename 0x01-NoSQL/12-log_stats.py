#!/usr/bin/env python3
""" stats about nginx logs """
from pymongo import MongClient


if __name__ == '__main__':
    client = MongoCLient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.find().count()} logs")
    print("Methods:")
    for meth in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        res = collection.find({method: meth}).count()
        print(f"\tmethod {meth}: {res}")
    res2 = collection.find({method: 'GET', path: '/status'}).count()
    print(f"{result} status check")
