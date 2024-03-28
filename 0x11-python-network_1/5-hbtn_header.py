#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    header = res.headers.get('X-Request-Id')
    print(header)
