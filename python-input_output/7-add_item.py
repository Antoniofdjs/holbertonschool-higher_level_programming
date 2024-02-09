#!/usr/bin/python3
"""load lists into a json file"""


import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
save_json(args, "add_item.json")
