#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    length = len(my_list)
    for i in range(1, length + 1):
        c = i * (-1)
        print("{:d}".format(my_list[c]))
