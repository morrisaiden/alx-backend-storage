#!/usr/bin/env python3
"""
a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
    """
    documents = mongo_collection.find()

    if mongo_collection.count_documents({}) == 0:
        return []

    return list(documents)
