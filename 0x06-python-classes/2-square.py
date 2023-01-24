#!/usr/bin/python3
"""
This module contains class Sqaure

"""
class Square:

    """
    Initialize an instace of Square

    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """
    Check if the size of the square is less than zero
    or Not an integer

    __size(int) = the size of the square

    """
