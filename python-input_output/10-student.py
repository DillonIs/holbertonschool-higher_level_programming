#!/usr/bin/python3
"""Class defined as Student based on 9-student.py"""


class Student():
    """Defines a class as Student"""
    def __init__(self, first_name, last_name, age):
        """Creates a new instance of Student
        and applies attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of Student"""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
