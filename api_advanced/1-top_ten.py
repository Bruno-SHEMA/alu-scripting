#!/usr/bin/python3
"""Module that queries the Reddit API for hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, OK if the request fails."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print("OK")

        results = response.json().get("data", {}).get("children", [])

        for post in results[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("OK")
