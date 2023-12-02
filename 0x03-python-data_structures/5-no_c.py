#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for i in range(len(my_string)):
        if not (my_string[i] == 'c' or my_string[i] == 'C'):
            string += my_string[i]
    my_string = string
    return my_string
