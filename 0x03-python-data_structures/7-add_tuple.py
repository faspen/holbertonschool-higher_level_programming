#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nt1 = tuple_a + (0, 0)
    nt2 = tuple_b + (0, 0)
    result_tup = (nt1[0] + nt2[0], nt1[1] + nt2[1])
    return result_tup
