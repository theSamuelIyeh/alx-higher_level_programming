#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except (IndexError, TypeError, ZeroDivisionError) as se:
        print("Exception: {}".format(se), file=sys.stderr)
        return None
