#!/usr/bin/python3
"""

Defines a function as add_integer(a, b=98) which is used to add a and b.

"""


def add_integer(a, b=98):
    """ Python function to add two integers and or floats as defined by a and b

    Arguments:
        a: first value
        b: second value

    Returns:
        The result of adding the two values

    Raises:
        TypeError: If a or b aren't integer and/or float

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
