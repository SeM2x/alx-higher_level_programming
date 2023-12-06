#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    for i in set_1:
        add = True
        for j in set_2:
            if (i == j):
                add = False
        if add:
            diff.append(i)

    for i in set_2:
        add = True
        for j in set_1:
            if (i == j):
                add = False
        if add:
            diff.append(i)
    return diff
