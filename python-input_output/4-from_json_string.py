#!/usr/bin/python3
"""JSON representation of an object (string):"""


import json


def from_json_string(my_str):
    '''
        change json str to python obj
    '''
    return json.loads((my_str))
