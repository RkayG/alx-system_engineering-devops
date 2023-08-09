#!/usr/bin/python3
""" queries an API and returns the required info"""
import requests
import json
import sys


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers)
    for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "my_reddit_api_v1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["data"]["subscribers"]
    else:
        return 0
