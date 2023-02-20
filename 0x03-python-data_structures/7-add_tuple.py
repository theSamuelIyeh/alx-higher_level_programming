#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_a_new = tuple_a
    tuple_b_new = tuple_b
    if len(tuple_a) < 2:
        if tuple_a == ():
            tuple_a_new = (0, 0)
        else:
            tuple_a_new = tuple_a + (0,)
    if len(tuple_b) < 2:
        if tuple_b == ():
            tuple_b_new = (0, 0)
        else:
            tuple_b_new = tuple_b + (0,)
    for i in range(0, 2):
        a = tuple_a_new[i]
        b = tuple_b_new[i]
        c = a + b
        new_tuple += (c,)
    return new_tuple
