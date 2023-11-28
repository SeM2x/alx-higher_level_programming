#!/usr/bin/python3
def print_last_digit(number):
    sign = -1 if number < 0 else 1
    digit = sign * (abs(number) % 10)
    print("{}".format(digit), end="")
    return digit
