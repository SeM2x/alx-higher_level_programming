#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_val = max(list(a_dictionary.values()))
        for key, val in a_dictionary.items():
            if max_val == val:
                return key
