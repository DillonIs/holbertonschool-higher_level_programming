#!/usr/bin/python3
"""Defines abstract class Shape
Using ABC package
Includes two abstract methods
Area and Perimeter
"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Defines class as Shape
    Inherits from ABC"""
    @abstractmethod
    def area(self):
        """Finds and returns the area
        of Shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Finds and returns the perimeter
        of Shape"""
        pass

class Circle(Shape):
    """Defines class as Circle
    Inherits from Shape"""
    def __init__(self, radius):
        """Creates an instance of Circle
        with a given radius"""
        self.radius = radius

    def area(self):
        """Finds and returns the area
        of Circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Finds and returns the perimeter
        of Circle"""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Defines class as Rectangle
    Inherits from Shape"""
    def __init__(self, width, height):
        """Creates an instance of Rectangle
        Defines the height and width"""
        self.height = height
        self.width = width

    def area(self):
        """Finds and returns the area
        of Rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Finds and returns the perimeter
        of Rectangle"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Formats and prints the info of Shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
