#!/usr/bin/python3
"""Class that inherits from list
Defined as MyList
"""


class MyList(list):
    """Arguments:
        list: To be sorted in ascending order
    """
    def print_sorted(self):
        """Prints list in ascending order"""
        list_ = self[:]
        list_.sort()
        print(list_)
