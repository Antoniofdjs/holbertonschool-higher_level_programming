#!/usr/bin/python3
""" This class defines a square, position and size
"""


class Square:
    """ class - Square defines a size
        defines area of square and position with tuple
    """
    def __init__(self, size=0, position=(0, 0)):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        return self.__size**2

# This will be the getter
    @property
    def size(self):
        return self.__size

# Its the setter
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

# Prints the square in # chars
    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for _ in range(0, self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

#position getter and setter
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) < 2:
            raise TypeError("value must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
