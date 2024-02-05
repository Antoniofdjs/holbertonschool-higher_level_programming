#!/usr/bin/python3
"""my class"""


class Rectangle:
    """empty rectangle"""
    def __init__(self, width=0, height=0):
        """init widht and height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """returns the visual str rectangle"""
        my_str = ""
        for _ in range(0, self.__height):
            my_str += "#" * self.__width
            my_str += "\n"
        return my_str.strip()

    def __repr__(self):
        """representation of class"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints bye message when del"""
        print("Bye rectangle...")
