#!/usr/bin/python3
""" CLass returns specified atribute if it has them
    it dictionary form
"""


class Student:
    """ Student class will return __dict__
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            has_atribute = {}
            for atribute in attrs:
                if hasattr(self, atribute):
                    has_atribute[atribute] = getattr(self, atribute)
        return has_atribute
