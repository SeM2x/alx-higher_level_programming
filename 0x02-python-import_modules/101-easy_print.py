#!/usr/bin/python3
if __name__ == "__main__":
    import os
    msg = "#pythoniscool\n"
    os.write(1, msg.encode())
