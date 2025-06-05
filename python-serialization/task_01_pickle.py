#!/usr/bin/python3
"""task_01_pickle"""
import pickle


class CustomObject:
    """Class defined as CustomObject"""
    def __init__(self, name, age, is_student):
        """Initializes an instance of CustomObject
        with attributes:
            name - Student name
            age - Student age
            is_student - Boolean to check if they are a student
        """
        self.name = name
        self.age = name
        self.is_student = is_student

    def display(self):
        """Prints the attributes of a class instance"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Method to serialize using Pickle module
        Parameters:
            filename - File to serialize to
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Loads an instance of CustomObject and returns it
        Parameters:
            filename - file to load and deserialize
        Retuns an instance
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
