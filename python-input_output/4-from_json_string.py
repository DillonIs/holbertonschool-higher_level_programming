#!/usr/bin/python3
"""Converts JSON string to object"""
import json


def from_json_string(my_str):
    """Returns the python representation of
    a JSON object"""
    return json.loads(my_str)
