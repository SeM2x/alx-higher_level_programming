#!/usr/bin/python3
import math
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
    TypeError: If either of a or b is a non-integer and non-float.
    """

    if (a == float("inf") or a == math.nan or
            (not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (b == float("inf") or b == math.nan or
            (not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
