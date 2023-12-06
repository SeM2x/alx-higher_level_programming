#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i, line in enumerate(matrix):
        new.append([])
        for j, element in enumerate(line):
            new[i].append(element ** 2)
    return new
