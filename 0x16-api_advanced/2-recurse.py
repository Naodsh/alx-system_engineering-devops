#!/usr/bin/python3
"""
2-recurse.py
This module contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles.
        after (str): The pagination parameter to get the next page of results.

    Returns:
        list: A list containing the titles of all hot articles, or None if the
              subreddit is invalid or no results are found.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data:
        return None

    posts = data.get('children', [])
    hot_list.extend([post['data']['title'] for post in posts])

    after = data.get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
