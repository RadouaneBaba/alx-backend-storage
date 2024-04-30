#!/usr/bin/env python3
""" chage all topics based on filter """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    mongo_collection.update_many({"name": name}, {"$set": {
          "topics": topics}})
