#!/usr/bin/python3
"""check directly or indirectly"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
