#!/usr/bin/python3
"""from json file"""

import json


def load_from_json_file(filename):
    """Load from json file"""

    with open(filename, "r") as file:
        """Getting from json"""

        myjson = json.loads(file.read())
        return myjson
