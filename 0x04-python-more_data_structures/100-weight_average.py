#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    count = 0
    for tup in my_list:
        sum += tup[0] * tup[1]
        count += tup[1]
    return sum/count
