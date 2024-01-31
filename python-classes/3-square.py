#!/usr/bin/python3
""" This class defines a square and size
"""


class Square:
    """ class - Square defines a size
        defines area of square
    """
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    def area(self):
        return self.__size**2
