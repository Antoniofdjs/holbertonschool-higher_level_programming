#!/usr/bin/python3
""" This class defines a square, position and size
"""


class Square:
    """ class - Square defines a size
        defines area of square and position with tuple
    """
    def __init__(self, size=0, position=(0, 0)):

        # Size related block
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        # The position related block
        if type(position) is not tuple or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size**2

# Getter for size
    @property
    def size(self):
        return self.__size

# Setter for size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

# position getter and setter
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) < 2:
            raise TypeError("value must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

# Print obect
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(0, self.__size):
                if self.__position[1] > 0 or self.position[0] == 0:
                    print('#' * self.__size)
                else:
                    print(' ' * self.__position[0] + '#' * self.__size)
