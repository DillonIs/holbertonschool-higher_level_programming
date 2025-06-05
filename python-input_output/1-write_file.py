#!/usr/bin/python3
"""Function that writes to a file"""


def write_file(filename="", text=""):
    """Writes text to filename"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
