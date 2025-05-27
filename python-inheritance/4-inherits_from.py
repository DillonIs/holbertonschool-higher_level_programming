#!/usr/bin/python3
"""Inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of an inherited class
    either directly or indirectly
    If not returns False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
