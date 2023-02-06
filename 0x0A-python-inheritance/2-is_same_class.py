#!/usr/bin/python3
"""
Check if object is instance of a class
"""


def is_same_class(obj, a_class):
    """ Check if its an instance of a class"""

    if not isinstance(obj, a_class):
        return False
    return True
