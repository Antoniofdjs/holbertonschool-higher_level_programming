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

    def from_json_string(json_string):
        """Convert json string into object again (list of dictionaries)"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turns data into json string"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json string into file, list of dictionaries"""
        if list_objs is None:
            list_objs = []

        file_name = str(cls.__name__) + ".json"

        # we make a list of dictionaries from objects
        list_of_dict = []
        for obj in list_objs:
            list_of_dict.append(obj.to_dictionary())

        with open(file_name, 'w') as f:
            # convert the list of dict to json and write in file
            json_string = cls.to_json_string(list_of_dict)
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates new instances of cls created"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        if cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance
