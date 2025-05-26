#!/usr/bin/python3
"""Python function that returns the list of attributes
and methods of an object"""


def lookup(obj):
    """Arguments:
        obj (class): short for object
    Returns:
        lists the available attributes and methods of an object
    """
    return dir(obj)
