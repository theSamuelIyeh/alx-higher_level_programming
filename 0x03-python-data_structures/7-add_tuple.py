#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    new_tuple = ()
    for i in range(0, 2):
        if tuple_a[i]:
            a = tuple_a[i]
        if tuple_b[i]:
            b = tuple_b[i]
        c = a + b
        new_tuple += (c,)
    return new_tuple
