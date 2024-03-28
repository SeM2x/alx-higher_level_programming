#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.."""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[2]

    res = requests.post(url, data={'q': q})
    try:
        json = res.json()
        if not json:
            print('No result')
        else:
            id = json.get('id')
            name = json.get('name')
            print(f'[{id}] {name}')
    except ValueError:
        print('Not a valid JSON')
