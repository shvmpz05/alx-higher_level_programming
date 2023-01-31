#!/usr/bin/bash
"""
creating a class called rectangle with an attribute width
"""


class Rectangle:
    """ Attribute width that is private"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (value < 0):
            raise ValueError("width must be >= 0")
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (value < 0):
            raise ValueError("height must be >= 0")
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        self.__height = value
