#!/usr/bin/python3
"""
Creating a file opening method
"""


def read_file(filename=""):

    """Opening file"""
    with open(filename, "r", encoding="UTF8") as file:
        print(file.read())
