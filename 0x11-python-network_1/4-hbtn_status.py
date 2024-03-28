#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    content = res.text
    print('Body response:')
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
