#!/usr/bin/python3
"""Write into file json representation"""


import json


def save_to_json_file(my_obj, filename):
    '''
        write json string into file
    '''
    j_object = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(j_object)
