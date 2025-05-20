#!/usr/bin/python3
"""Define a class as Square based on 2-square.py"""


class Square:
    """Define the properties of Square
    Instances:
    size - Private instance
    area - Public instance
    size must be a positive integer otherwise raise errors
    """
    def __init__(self, size=0):
        """Private instance of Square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Finds the area of Square
        Returns: The current square area
        """
        return self.__size ** 2
