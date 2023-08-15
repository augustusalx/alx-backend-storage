#!/usr/bin/env python3
"""
This module have utility function that lists all document
"""
import pymongo


def list_all(mongo_collection):
    """
    list all the collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
