#!/usr/bin/python3
"""
Module Name: 3-say_my_name
Description: prints name and last name
Authors: Lusanco, Ltoro9, Antoniofdjs, Livanhernandez Date: Feb 01 2024
"""


def say_my_name(first_name, last_name=""):
    """Description: prints first name and last name
    - first_name (str): The name string
    - last_name (str): The last name, default is \" \" """

    first = "first_name must be a string"
    last = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(first)
    if not isinstance(last_name, str):
        raise TypeError(last)
    if last_name is "":
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
