#!/usr/bin/python3
"""Function that returns True based on checks
Checks:
    if the object is an instance of
    or if the object is an instance of a class that inherited
    specified class
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is instance of:
        obj
        a_class
    Returns: True or False
    """
    return isinstance(obj, a_class)
