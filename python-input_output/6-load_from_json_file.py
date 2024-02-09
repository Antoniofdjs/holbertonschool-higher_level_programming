#!/usr/bin/python3
"""get json string from file"""


import json


def load_from_json_file(filename):
    '''
        unpack file with json string
    '''
    with open(filename, 'r') as f:
        return json.load(f)
