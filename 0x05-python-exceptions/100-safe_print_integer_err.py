#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        print()
    except ValueError as ve:
        print("Exception :", ve, file = sys.stderr)
safe_print_integer_err("ss")
