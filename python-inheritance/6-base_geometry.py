#!/usr/bin/python3
"""Defines BaseGeometry as a class based on 5-base_geometry.py"""


class BaseGeometry:
    """Creates an instance of BaseGeometry"""
    def area(self):
        """Raises an Exception if area is not implemented"""
        raise Exception("area() is not implemented")
