#!/usr/bin/python3
"""Defines a class as Square based on 9-rectangle.py
Square inherits Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """Generates an instance of Square
        Defines the size of Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Finds and returns the area of Square"""
        return self.__size ** 2
