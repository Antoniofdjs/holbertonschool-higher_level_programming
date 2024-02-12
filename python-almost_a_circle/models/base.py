#!/usr/bin/python3
""" Base Class
"""


class Base:
    """
    will manage id for other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init for id of classes
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
