#!/usr/bin/python3
"""Defines a class as VerboseList
Extends the Python list class"""


class VerboseList(list):
    """Adds notifications for list operations"""

    def append(self, item):
        """Updates an item to the list
        with notification"""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        """Used to extend the list
        with notification"""
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """Deletes the first occurence of an item
        from the list with notification
        Raises:
            ValueError: when the item isn't found
        """
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """Deletes and returns an item at index
        with notfication"""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
