#!/usr/bin/python3
"""class geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from baseG
    it also validates integers thanks to inheritance
    """
    def __init__(self, width, height):
        Rectangle.integer_validator("width", width)
        Rectangle.integer_validator("height", height)
        self.__width = width
        self.__height = height
