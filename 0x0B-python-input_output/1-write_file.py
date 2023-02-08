#!/usr/bin/python3
""" Writing to a file"""


def write_file(filename="", text=""):
    """Writing characters to file"""

    with open(filename, "w", encoding="UTF8") as file:
        mychars =  file.write(text)
    return mychars
