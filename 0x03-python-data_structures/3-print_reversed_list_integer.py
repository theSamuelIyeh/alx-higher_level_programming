#!/usr/bin/python3
def print_reversed_list_integer(my_list = []):
    length = len(my_list)
    for i in range(length, 0):
        c = i * (-1)
        print("{:d}".format(my_list[c]))
