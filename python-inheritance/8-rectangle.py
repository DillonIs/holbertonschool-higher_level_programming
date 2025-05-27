#!/usr/bin/python3
"""Defines a class as Rectangle that inherits BaseGeometry
based on 7-base_geometry.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates an instance of Rectangle"""
    def __init__(self, width, height):
        """Instance of Rectangle
        Defines the width and height of Rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
