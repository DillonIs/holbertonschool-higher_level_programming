#!/usr/bin/python3
"""Function that prints a square with the character #
Variable:
size is the size of the square to be printed
"""


def print_square(size):
    """size (int): The size of the square

    Raises:
        TypeError: If size is not an integer and is less than 0
        ValueError: If size is less than 0
    """
    message = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(message)
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
