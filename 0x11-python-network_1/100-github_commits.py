#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
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

    commits = sorted(res.json(), key=lambda x: x.get(
        'commit').get('committer').get('date'), reverse=True)[:10]
    for commit in commits:
        print(f"{commit.get('sha')}: {commit.get(
            'commit').get('author').get('name')}")
