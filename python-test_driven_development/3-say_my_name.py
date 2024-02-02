#!/usr/bin/python3
"""
Module Name: 3-say_my_name
Description: prints name and last name
Author: Lusanco,Antonio, Louis Date: Feb 01 2024
"""


def say_my_name(first_name, last_name=""):
    """Description: prints first name and last name
    - first_name (str): The name string
    - last_name (str): The last name, default is '' """

    error_a = "first_name must be a string"
    error_b = "last_name must be a string"

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if first_name != "" and last_name != "":
        print("My name is {} {}".format(first_name, last_name))
    elif first_name != "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {}".format(last_name))
