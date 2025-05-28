#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Defines class as Animal
    inherits from ABC"""

    @abstractmethod
    def sound(self):
        """Abstract method defines the sound Animals make"""
        pass

class Dog(Animal):
    """Class defined as Dog
    Inherits from Animal"""
    def sound(self):
        """Defines and returns the sound a dog makes"""
        return "Bark"

class Cat(Animal):
    """Class defined as Cat
    Inherits from Animal"""
    def sound(self):
        """Defines and returns the sound a cat makes"""
        return "Meow"
