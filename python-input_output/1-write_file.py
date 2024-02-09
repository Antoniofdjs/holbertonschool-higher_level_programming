#!/usr/bin/python3
'''
    0-read_file.py
    Description: Write a function that reads a
    text file (UTF8) and prints it to stdout
'''


def write_file(filename="", text=""):
    '''
        writes in text file, returns the number of chars written:
    '''
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(text)
        return len(text)
