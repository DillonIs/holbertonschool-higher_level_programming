#!/usr/bin/python3
"""Task based on 10-square.py
Class defined as Square that inherits from Rectangle
Based on 9-rectangle.py
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

    def __str__(self):
        """Represents Square as a string"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Finds and returns the area of Square"""
        return self.__size ** 2
