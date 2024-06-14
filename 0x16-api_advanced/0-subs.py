#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit. If an invalid subreddit is given, the
function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'reddit-subscriber-counter/0.1 by u/UnfairArtist8484',
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Debugging information
        print(f"Status Code: {response.status_code}")
        #print(f"Response Content: {response.text}")

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscriber']
        else:
            return 0
    except requests.RequestException as e:
        print(f"RequestException: {e}")
        return 0
