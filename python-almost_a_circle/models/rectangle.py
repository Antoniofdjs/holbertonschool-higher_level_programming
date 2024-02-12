#!/usr/bin/python3

"""
Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle with id, width, height, x, and y"""
        self.validator("width", width)
        self.validator("height", height)
        self.validator("x", x)
        self.validator("y", y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validator(self, flag, value):
        """Validation function for Rectangle"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(flag))
        else:
            if (flag == "width" or flag == "height") and value <= 0:
                raise ValueError("{} must be > 0".format(flag))
            if (flag == "x" or flag == "y") and value < 0:
                raise ValueError("{} must be >= 0".format(flag))

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """ Prints rectangle shape with # """
        for row in range(self.__height):
            print(str('#'*self.__width))

    def __str__(self):
        """str representation """
        my_str = "[Rectangle] ({}) ".format(self.id)
        my_str += "{}/{} ".format(self.__x, self.__y)
        my_str += "- {}/{}".format(self.__width, self.__height)
        # [Rectangle] (<id>) <x>/<y> - <width>/<height>
        return my_str

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        self.validator("y", value)
        self.__y = value
