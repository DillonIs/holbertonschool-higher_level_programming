#!/usr/bin/python3
"""Class defined as Rectangle based on 7-rectangle.py"""


class Rectangle:
    """Attributes:
        width (int): Defines the width of the rectangle
        height (int): Defines the height of the rectangle
    """
    number_of_instances = 0
    """Above counts the instances"""
    print_symbol = "#"
    """Above uses the symbol to visualise Rectangle"""

    def __init__(self, width=0, height=0):
        """Creates a private instance of Rectangle
        with width and height default set to 0"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter for width
        Returns the value of width"""
        return self.__width

    @property
    def height(self):
        """Getter for height
        Returns the value of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is negative"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is negative"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Finds and returns the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Finds and returns the perimeter of Rectangle
        Returns 0 if either height or width is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints Rectangle as certain characters"""
        rectangle = []
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")
        rectangle.pop()
        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of Rectangle"""
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to find the larger rectangle based on area
        Returns rect_1 if both Rectangles are equal
        Raises:
            TypeError: if rect_1 is not in an instance of Rectangle
            TypeError: if rect_2 is not in an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
