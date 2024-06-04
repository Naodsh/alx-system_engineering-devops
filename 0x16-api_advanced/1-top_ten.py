#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and print the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts of the specified subreddit.

    Args:
        subreddit (str): The name of the subreddit to search for.

    Returns:
        None
    """
    try:
        # Send HTTP GET request to Reddit API
        response = requests.get(
                f"https://www.reddit.com/r/{subreddit}/hot.json",
                headers={"User-Agent": "Top Ten Reddit Posts"})
        response.raise_for_status()  # Raise error if request was unsuccessful

        # Extract titles from JSON response
        data = response.json()
        posts = data['data']['children']

        # Print titles of the first 10 hot posts
        for post in posts[:10]:
            print(post['data']['title'])
    except Exception as e:
        print(None)
