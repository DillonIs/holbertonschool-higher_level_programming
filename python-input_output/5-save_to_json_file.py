#!/usr/bin/python3
"""Writes an object to a file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Saves to a JSON file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
