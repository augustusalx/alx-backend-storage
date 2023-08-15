#!/usr/bin/env python3
"""
to find by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    To find by topic
    """
    return mongo_collection.find({"topics": topic})
