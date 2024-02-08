#!/usr/bin/python3
"""Returns true or false if obj is a_class"""


def is_same_class(obj, a_class):
    """
    Write a function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    """
    return type(obj) == a_class
