#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.."""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    res = requests.get(
        url=f"https://api.github.com/repos/{owner}/{repo}/commits", headers=headers)

    commits = res.json()
    for commit in commits:
        print(f"{commit.get('sha')}: {commit.get(
            'commit').get('author').get('name')}")
