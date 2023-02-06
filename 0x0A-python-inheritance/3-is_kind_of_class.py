#!/usr/bin/python3
"""
Check if its instance and also if there is any inheritance
"""


def is_kind_of_class(obj, a_class):
    """ Check for instance """

    if not isinstance(obj, a_class):
        return False
    return True
