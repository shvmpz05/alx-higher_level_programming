#!/usr/bin/python3
"""
This module will create a class Square and allow to get the area
"""


class Square:

    """Initialize a sqaure and the dimensions"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
