#!/usr/bin/python3
"""
Raising exceptions
"""


class BaseGeometry:

    """ Methid to raise exception """
    def area(self):
        raise Exception("area() is not implemented")
