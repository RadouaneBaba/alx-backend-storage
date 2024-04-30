#!/usr/bin/env python3
""" stats about nginx logs """
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    for meth in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        res = collection.count_documents({"method": meth})
        print(f"\tmethod {meth}: {res}")
    res2 = collection.count_documents({"method": 'GET', "path": '/status'})
    print(f"{res2} status check")
