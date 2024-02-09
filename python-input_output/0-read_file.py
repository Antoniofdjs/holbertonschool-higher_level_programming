#!/usr/bin/python3
'''
    0-read_file.py
    Description: Write a function that reads a
    text file (UTF8) and prints it to stdout
'''



def read_file(filename=""):
    '''
        Function that reads a text file (UTF8) and prints it to stdout
    '''
    with open(filename, 'r', encoding='utf-8') as my_file:
        content = my_file.read()
        print("{}".format(content),end='')
