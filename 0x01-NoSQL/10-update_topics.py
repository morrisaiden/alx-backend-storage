#!/usr/bin/env python3
"""
a Python function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
        name (_type_): _description_
        topics (_type_): _description_
    """
    
    return mongo_collection.update_many(
        {
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        }
    )