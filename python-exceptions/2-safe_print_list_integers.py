#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end='')
            result += 1
        except (ValueError, TypeError):
            pass
    print()
    return (result)
