#!/usr/bin/python3
"""Append to file method"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="UTF8") as file:
        mychar = file.write(text)
    return mychar
