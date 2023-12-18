#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as ze:
        print("Exception: {}".format(ze), file=sys.stderr)
    except IndexError as ie:
        print("Exception: {}".format(ie), file=sys.stderr)
