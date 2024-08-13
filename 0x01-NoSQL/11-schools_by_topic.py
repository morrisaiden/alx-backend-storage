#!/usr/bin/env python3
"""
a Python function that returns the list of school having a specific topic
"""
import pymongo

def schools_by_topic(mongo_collection, topic):
    """_summary_

    Args:
        schools (_type_): _description_
        topic (_type_): _description_
    """
    return mongo_collection.find(
        {
            "topics": topic
        }
    )