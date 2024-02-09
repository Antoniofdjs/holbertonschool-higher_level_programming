#!/usr/bin/python3
""" This function reads a file 
and writesto stdout
"""


def read_file(filename=""):
    """This is prints """
    with open(filename, 'r', encoding='utf-8') as my_file:
        content = my_file.read()
        print("{}".format(content),end='')
