#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list = [item for i, item in enumerate(my_list) if i != idx]
    return my_list
