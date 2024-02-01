#!/usr/bin/python3
"""
Functions that adds two integers.
a and b must be integers or floats, otherwise raise a TypeError
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
