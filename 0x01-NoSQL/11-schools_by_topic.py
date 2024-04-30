#!/usr/bin/env python3
""" returns list of topic """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    mongo_collection.find({ "topic": topic })
