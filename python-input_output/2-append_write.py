#!/usr/bin/python3
"""Append to file"""


def append_write(filename="", text=""):
    '''
        append in text file, returns the number of chars written:
    '''
    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
        return len(text)
