#!/usr/bin/python3
"""Defines a class as CountedIterator
Used to count the iterations of the iter function
"""


class CountedIterator:
    """Counts the number of items iterated"""
    def __init__(self, iterable):
        """Creates an instance and counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Icrements the count and returns the next item"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Current count"""
        return self.count

    def __iter__(self):
        """Returns the iterator"""
        return self
