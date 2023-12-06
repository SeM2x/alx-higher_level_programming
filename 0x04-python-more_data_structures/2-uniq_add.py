#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    res = 0
    for element in unique:
        res += element
    return res
