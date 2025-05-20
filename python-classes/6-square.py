#!/usr/bin/python3
"""Define a class as Square based on 5-square.py"""


class Square:
    """
    Define the properties of Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instances of Square
        size (int): The size of the square
        position (tuple): The position of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Finds and returns the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for attribute position
        Raises:
            TypeError when position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints Square as #s"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
