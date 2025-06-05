#!/usr/bin/python3
"""Function that appends a file"""


def append_write(filename="", text=""):
    """Appends text to a file
    text is the string to append"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
