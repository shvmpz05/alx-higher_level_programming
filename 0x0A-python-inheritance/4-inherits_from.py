#!/usr/bin/python3
"""
Checks if it inherits
"""


def inherits_from(obj, a_class):
    """Check if it inherits"""

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
