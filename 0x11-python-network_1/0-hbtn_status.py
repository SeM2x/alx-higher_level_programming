#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as res:
    content = res.read()
    print('Body response:')
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
