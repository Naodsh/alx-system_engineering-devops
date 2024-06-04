import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or an error occurs, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "alxRedditBot"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        return 0
