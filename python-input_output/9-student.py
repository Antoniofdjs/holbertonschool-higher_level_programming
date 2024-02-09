#!/usr/bin/python3
""" Write a class Student that defines a student
    it also  returns the class dictionary
"""


class Student:
    """ Student class will return __dict__
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
