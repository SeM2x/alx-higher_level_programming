#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for item in line:
            print("{:d}".format(item), end=" ")
        print()
