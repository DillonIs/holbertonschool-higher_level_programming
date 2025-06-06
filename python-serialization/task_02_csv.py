#!/usr/bin/python3
"""task_02_csv"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a csv file into a JSON file"""
    try:
        """Serializes and deserializes
        Returns True if serialisation and deserialization has occurred"""
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_read = csv.DictReader(csv_file)
            data = [row for row in csv_read]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        """Returns False if the file doesn't exist"""
        return False

if __name__ == "__main__":
    csv_file = "data.csv"
    success = convert_csv_to_json(csv_file)
    if success:
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"Failed to convert data from {csv_file}")
