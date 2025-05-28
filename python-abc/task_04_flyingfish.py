#!/usr/bin/python3
"""Multiple inheritance
Class defined as FlyingFish
Inherits from both Fish and Bird classes"""


class Fish:
    """Class defined as Fish
    Method:
        swim - prints The fish is swimming
        habitat - prints The fish lives in water
    """
    def swim(self):
        """Prints The fish is swimming"""
        return "The fish is swimming"

    def habitat(self):
        """Prints The fish lives in water"""
        return "The fish lives in water"

class Bird:
    """Class defined as Bird
    Method:
        fly - prints The bird is flying
        habitat - prints The bird lives in the sky
    """
    def fly(self):
        """Prints The bird is flying"""
        return "The bird is flying"

    def habitat(self):
        """Prints The bird lives in the sky"""
        return "The bird lives in the sky"

class FlyingFish(Fish, Bird):
    """Class defined as FlyingFish
    Inherits from both Fish and Bird"""
    def fly(self):
        """Prints The flying fish is soaring!"""
        return "The flying fish is soaring!"

    def swim(self):
        """Prints The flying fish is swimming!"""
        return "The flying fish is swimming!"

    def habitat(self):
        """Prints The flying fish lives both in water and the sky!"""
        return "The flying fish lives both in water and the sky!"

if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())
