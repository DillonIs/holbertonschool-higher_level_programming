#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """pascal_triangle function"""

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) is not n:
        """coef is the coefficient
        triangle is the 2D array"""
        coef = [1]
        for i in range(len(triangle[-1]) - 1):
            coef.append(triangle[-1][i] + triangle[-1][i + 1])
        coef.append(1)
        triangle.append(coef)
    return triangle
