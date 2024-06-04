#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""


import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Define the URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Define headers to set a custom User-Agent
    headers = {'User-Agent': 'MyRedditClient/0.1'}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # Return 0 for any unsuccessful requests
            return 0
    except requests.RequestException:
        # Return 0 if there is a request exception
        return 0
