#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    ac = len(sys.argv)
    av = sys.argv
    res = 0
    for i in range(ac - 1):
        res += int(av[i + 1])
    print("{}".format(res))
