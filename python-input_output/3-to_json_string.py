#!/usr/bin/python3
"""JSON representation of an object (string):"""


import json


def to_json_string(my_obj):
    '''
        change obj to json representation
    '''
    return json.dumps((my_obj))
