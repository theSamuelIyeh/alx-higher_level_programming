#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i > x or i == x:
            continue
        if i == 8 and x == 9:
            print("{}{}".format(i, x))
        else:
            print("{}{}, ".format(i, x), end="")
