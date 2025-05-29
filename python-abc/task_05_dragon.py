#!/usr/bin/python3
"""Dragon class with mixins"""


class SwimMixin:
    """Mixin class for Swim"""
    def swim(self):
        """Method defines swim
        Prints - The creature swims!"""
        print("The creature swims!")

class FlyMixin:
    """Mixin class for Fly"""
    def fly(self):
        """Method defines fly
        Prints - The creature flies!"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class
    Additional Method:
        roar - Prints The dragon roars!"""
    def roar(self):
        """Method defines roar
        Prints - The dragon roars!"""
        print("The dragon roars!")
