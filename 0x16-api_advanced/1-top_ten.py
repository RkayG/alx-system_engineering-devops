#!/usr/bin/python3
""" queries an API and prints required info"""
import requests
import json


def top_ten(subreddit):
    """queries the Reddit API and
    prints the titles of the first
    10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my_reddit_api_v1"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        [print(c.get("data").get("title")) for c in data.get("children")]
    else:
        print("None")
