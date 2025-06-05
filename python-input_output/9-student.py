#!/usr/bin/python3
"""Student to JSON"""


class Student():
    """Defines a class as Student"""
    def __init__(self, first_name, last_name, age):
        """Creates a new instance of Student
        and applies attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of Student"""
        return self.__dict__
