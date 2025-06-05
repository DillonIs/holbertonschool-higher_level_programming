#!/usr/bin/python3
"""task_00_basic_serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes and saves a Python dictionary to a JSON file
    Parameters:
        data - Python dictionary
        filename - Output JSON file if output exists replace
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file
    Parameter:
        filename - File to deserialize
    Returns: Python dictionary
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
