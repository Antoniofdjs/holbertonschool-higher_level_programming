#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    error_a = "first_name must be a string"
    error_b = "last_name must be a string"

    if first_name is None:
        raise TypeError(error_a)
    if last_name is None:
        raise TypeError(error_b)
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if last_name is not "":
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
