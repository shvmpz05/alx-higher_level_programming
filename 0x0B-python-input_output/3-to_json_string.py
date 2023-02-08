#!/usr/bin/python3
"""IMport json module"""

import json


def to_json_string(my_obj):
    """Return json format of object"""

    myjson = json.dumps(my_obj)
    return myjson
