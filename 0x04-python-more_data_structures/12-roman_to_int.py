#!/usr/bin/python3
def roman_to_int(roman_string):
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    num = 0
    size = len(roman_string)
    for i in range(size):
        c = roman_string[i]
        if i < size - 1:
            next_c = roman_string[i + 1]
        if c == 'I' and next_c != 'I':
            num -= symbols[c]
        else:
            num += symbols[c]
    return num
