def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "alxRedditBot")

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        return 0
