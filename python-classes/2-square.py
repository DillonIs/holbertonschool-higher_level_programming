#!/usr/bin/python3
"""Define a class as Square based on 1-square.py"""


class Square:
    """Define the properties of Square
    Attributes:
    size
    size must be an integer and greater than or equal to 0
    """
    def __init__(self, size=0):
        """Generates a new instance of Square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
