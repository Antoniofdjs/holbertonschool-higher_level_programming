#!/usr/bin/python3
""" Base Class
"""

import json


class Base:
    """
    will manage id for other classes and json string method
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turns dictionaries into json string"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        file_name = str(cls.__name__) + ".json"
        with open(file_name, 'w') as f:
            for object in list_objs:
                dictionary = object.to_dictionary()
                json_string = cls.to_json_string(dictionary)
                f.write(json_string)
