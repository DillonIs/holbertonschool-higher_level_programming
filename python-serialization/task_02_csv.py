#!/usr/bin/python3
"""task_02_csv"""
import csv
import json


def convert_csv_to_json(csv_file):
    """Converts a csv file into a JSON file"""
    try:
        """Serializes and deserializes
        Returns True if serialisation and deserialization has occurred"""
        with open('data.csv', 'r', encoding='utf-8') as csv_file:
            data = list(csv.DictReader(csv_file))
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        """Returns False if the file doesn't exist"""
        return False
