#!/usr/bin/python3
"""class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from geometry and rectangle
    it also validates integers thanks to inheritance
    it calculates area and has str representation
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area (self):
        return self.__size ** 2
    
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
