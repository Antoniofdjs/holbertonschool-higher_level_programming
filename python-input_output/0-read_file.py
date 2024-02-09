#!/usr/bin/python3
""" This function reads a file and writes
to stdout
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as my_file:
        content = my_file.read()
        print("{}".format(content))
