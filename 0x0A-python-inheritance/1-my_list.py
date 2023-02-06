#!/usr/bin/python3
"""
Class that inherits from class list
"""


class MyList(list):

    """ Sort the list given by the user"""

    def print_sorted(self):
        self.sort()
        print(self)
