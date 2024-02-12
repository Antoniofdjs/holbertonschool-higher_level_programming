#!/usr/bin/python3
"""  Class Rectangle inhertis from Base
"""

from models.base import Base


class Rectangle(Base):
    """
        Rectangle sub class of Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.int_validator("width", width)
        self.int_validator("height", height)
        self.int_validator("x", x)
        self.int_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def int_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validator("width", value)
        self.__width = value

    @property
    def heigth(self):
        return self.__height

    @heigth.setter
    def height(self, value):
        self.int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.int_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.int_validator("y", value)
        self.__y = value
