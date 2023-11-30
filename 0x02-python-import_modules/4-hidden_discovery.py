#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4
    for v in dir(hidden_4):
        if (v[0] != '_'):
            print(v)
