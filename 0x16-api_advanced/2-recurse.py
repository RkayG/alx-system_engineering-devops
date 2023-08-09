#!/usr/bin/python3
""" queries an api and returns required info."""
import requests


def recurse(subreddit, after="", hotlist=[], count=0):
    """
    recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my_reddit_api_v1"}
    params = {
              'after': after,
              'count': count,
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        children = response.json().get("data").get("children")
        after = response.json().get("data").get("after")
        count += response.json().get("data").get("dist")
        for i in children:
            hotlist.append(i.get("data").get("title"))
        count += 1
        if after is not None:
            recurse(subreddit, after, hotlist, count)
        if len(hotlist) == 0:
            return None
        return hotlist
    else:
        return None
