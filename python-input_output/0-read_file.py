#!/usr/bin/python3
"""Python function that reads a text file"""


def read_file(filename=""):
    """Prints a UTF8 file after reading the file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
