#!/usr/bin/python3
"""
load class into json print description
of atributes
"""


def class_to_json(obj):
    """returns dcitionary of all atributes of class"""
    return obj.__dict__
