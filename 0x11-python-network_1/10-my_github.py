#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.."""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {password}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    res = requests.get(
        url=f" https://api.github.com/users/{username}", headers=headers)
    if res.ok:
        print(res.json().get('id'))
    else:
        print(None)
