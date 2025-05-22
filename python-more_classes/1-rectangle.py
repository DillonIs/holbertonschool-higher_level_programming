#!/usr/bin/python3
"""Class defined as Rectangle based on 0-rectanle.py"""


class Rectangle:
    """Attributes:
        width (int): Defines the width of the rectangle
        height (int): Defines the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Creates an instance of Rectangle
        width and height default at 0"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width
        Returns the value of width"""
        return self.__width

    @property
    def height(self):
        """Getter for height
        Returns the value of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is negative"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is negative"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
