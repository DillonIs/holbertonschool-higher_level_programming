#!/usr/bin/python3
"""Function for dividing all elements of a matrix.

Function prototype:
    matrix_divided
"""


def matrix_divided(matrix, div):
    """Variables:
        matrix: A list of lists of integers and/or floats
        div: Value used to divide by

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If each row of the matrix sizes do not match
        TypeError: If any value of the matrix is not an integer or float
        TypeError: If a row in the matrix is not a list
        TypeError: If div is not a float or integer
        ZeroDivisionError: If div is equal to zero

    Returns:
        The result of the division
"""
    row = None
    message = "matrix must be a matrix (list of lists) of integers/floats"
    zero_msg = "division by zero"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)
    for ind in matrix:
        if not ind or not isinstance(ind, list):
            raise TypeError(message)
        for value in ind:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError(message)
        if row is None:
            row = len(ind)
        elif row != len(ind):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError(zero_msg)
    new_matrix = [[round(value / div, 2) for value in ind] for ind in matrix]
    return new_matrix
