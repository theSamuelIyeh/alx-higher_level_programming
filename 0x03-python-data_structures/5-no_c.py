#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char == "C" or char == "c":
            continue
        new_string += char
    return new_string
