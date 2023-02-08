#!/usr/bin/python3
"""Convert to JSON"""

import json


def to_json_string(my_obj):
    myjson = json.dumps(my_obj)
    return myjson
