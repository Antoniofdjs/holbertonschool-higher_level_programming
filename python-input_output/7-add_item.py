#!/usr/bin/python3
"""get json string from file"""


import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

my_list = []


try:
    my_list = load_json("add_item.json")[:]
except FileNotFoundError:
    pass


args = sys.argv[1:]
my_list.extend(args)


save_json(my_list, "add_item.json")
