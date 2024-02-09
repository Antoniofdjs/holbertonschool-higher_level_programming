#!/usr/bin/python3
"""get json string from file"""


import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

my_list = []

# load list from json if file.json exists
try:
    my_list = load_json("add_item.json")[:]
except FileNotFoundError:
    pass

# get args from the user to add to list
args = sys.argv[1:]
my_list.extend(args)

# finally save into .json file for future use
save_json(my_list, "add_item.json")
