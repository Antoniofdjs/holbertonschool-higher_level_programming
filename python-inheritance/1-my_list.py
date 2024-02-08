#!/usr/bin/python3
"""my list inherits from list"""


class MyList(list):
    """MyList will print inheritance from list"""
    def print_sorted(self):
        print(sorted(self))
