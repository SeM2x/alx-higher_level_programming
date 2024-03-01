#!/usr/bin/python3
"""defines pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal's triangle of n

    Args:
        n (int): n

    Returns:
        [list]: pascal
    """
    if n <= 0:
        return []
    pascal = [[1]]
    i = 0
    while (i < n - 1):
        prev = pascal[i]
        row = [1] + [prev[j] + prev[j + 1]
                     for j in range(len(prev) - 1)] + [1]
        pascal.append(row)
        i += 1
    return pascal
