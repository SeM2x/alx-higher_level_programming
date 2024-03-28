#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    res = requests.get(
        url=f"https://api.github.com/repos/{owner}/{repo}/commits")

    commits = res.json()
    for commit in commits:
        print(f"{commit.get('sha')}: {commit.get(
            'commit').get('author').get('name')}")
