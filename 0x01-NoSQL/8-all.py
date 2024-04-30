#!/usr/bin/env python3
""" list all documents in collection """


def list_all(mongo_collection):
    """ list all docs """
    return mongo_collection.find()
