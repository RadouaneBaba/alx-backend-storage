#!/usr/bin/env python3
""" insert new document """


def insert_school(mongo_collection, **kwargs):
    """ insert new document collection based on kwargs """
    return mongo_collection.insert_one(kwargs).inserted_id
