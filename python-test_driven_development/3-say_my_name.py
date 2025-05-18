#!/usr/bin/python3
"""Function for printing a name
Prints a name
"""


def say_my_name(first_name, last_name=""):
    """Variables:
    first_name(str): First name
    last_name(str): Last name

    Raises:
        TypeError: If either name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
