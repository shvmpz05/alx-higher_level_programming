#!/usr/bin/python3
"""Import json and method for right into json file"""


import json


def save_to_json_file(my_obj, filename):
    """Open and write into file"""

    with open(filename, "w") as file:
        myjson = json.dumps(my_obj)
        file.write(myjson)
