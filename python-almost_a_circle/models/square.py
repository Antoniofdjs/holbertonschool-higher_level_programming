#!/usr/bin/python3
""" Square Class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square, inherits from Rectangle and Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation """
        my_str = "[Square] ({}) ".format(self.id)
        my_str += "{}/{} ".format(self.x, self.y)
        my_str += "- {}".format(self.width)
        # "[Rectangle] (<id>) <x>/<y> - <width>"
        return my_str

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validator("width", value)
        self.width = value
        self.height = value
