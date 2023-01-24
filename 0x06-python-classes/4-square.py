#!/usr/bin/python3

""" This module will create a class Square and allow to get the area """


class Square:

    """Initialize a sqaure and the dimensions"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size ** 2

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
