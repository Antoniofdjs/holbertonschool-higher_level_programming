#!/usr/bin/python3
"""Write into file json representation"""


import json


def save_to_json_file(my_obj, filename):
    '''
        write json string into file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dumps(my_obj, f)
