#!/usr/bin/python3
"""Defines a class as Rectangle that inherits BaseGeometry
based on 8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class defined as Rectangle"""
    def __init__(self, width, height):
        """Creates an instance of Rectangle
        Defines width and height of Rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Finds and returns the area of Rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Represents Rectangle as a string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
