#!/usr/bin/python3
"""Define a class as Square based on 3-square.py"""


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

    def area(self):
        """Finds the square area
        Returns: The square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for attribute
        note: Tried get and set as get_size and set_size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
