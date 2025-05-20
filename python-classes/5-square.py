#!/usr/bin/python3
"""Define a class as Square based on 4-square.py"""


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
        """Finds and returns Square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for attribute"""
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

    def my_print(self):
        """Prints Square as #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
