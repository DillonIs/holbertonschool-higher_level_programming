#!/usr/bin/python3
"""Defines a class as BaseGeometry
based on 6-base_geometry.py
"""


class BaseGeometry:
    """Creates an instance of BaseGeometry"""
    def area(self):
        """Raises an Exception if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value, assumes name is always a string
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
