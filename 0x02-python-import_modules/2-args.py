#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    print("{}".format(argc - 1), end=" ")
    if (argc == 1):
        print("arguments.")
    else:
        if (argc == 2):
            print("argument:")
        else:
            print("arguments:")

        for i in range(argc - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
