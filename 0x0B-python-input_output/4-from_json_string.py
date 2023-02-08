#!/usr/bin/python3
"""Import json"""

import json


def from_json_string(my_str):
    """Return python data structure"""

    mydata = json.loads(my_str)
    return mydata
