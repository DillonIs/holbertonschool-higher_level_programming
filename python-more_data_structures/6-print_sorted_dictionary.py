#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())
    for keys in sorted_dict:
        print("{}: {}".format(keys, a_dictionary[keys]))
