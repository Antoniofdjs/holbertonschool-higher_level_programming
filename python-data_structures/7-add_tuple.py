#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    total_0 = 0
    total_1 = 0
    if len(tuple_a) >= 1:
        total_0 += tuple_a[0]
    if len(tuple_b) >= 1:
        total_0 += tuple_b[0]
    if len(tuple_a) >= 2:
        total_1 += tuple_a[1]
    if len(tuple_b) >= 2:
        total_1 += tuple_b[1]
    return (total_0, total_1)
