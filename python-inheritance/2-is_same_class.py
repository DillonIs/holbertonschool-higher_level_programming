#!/usr/bin/python3
"""Function that returns True
Only if the object is exactly an instance
of specified class
Otherwise False
"""


def is_same_class(obj, a_class):
    """Returns True when obj is an
    instance of a_class"""
    if type(obj) is a_class:
        return True
    return False
