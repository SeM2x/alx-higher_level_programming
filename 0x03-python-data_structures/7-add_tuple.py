#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    max_length = max(len(tuple_a), len(tuple_b))
    tuple_a += (0,) * (max_length - len(tuple_a))
    tuple_b += (0,) * (max_length - len(tuple_b))
    for item1, item2 in zip(tuple_a, tuple_b):
        new += (item1 + item2,)
    return new
