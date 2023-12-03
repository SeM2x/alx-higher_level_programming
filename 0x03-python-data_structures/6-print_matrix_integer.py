#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, item in enumerate(line):
            print("{:d}".format(item), end="")
            if i < len(line) - 1:
                print(" ", end="")
        print()
