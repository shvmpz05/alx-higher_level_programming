#!/usr/bin/python3
"""
Raising exceptions
"""


class BaseGeometry:

    """ Methid to raise exception """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """ validation """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
