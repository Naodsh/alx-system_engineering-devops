#!/usr/bin/python3
"""
100-count.py
This module contains a recursive function that queries the Reddit API, parses
the titles of all hot articles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API, parses the titles of hot articles, and prints a
    sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The pagination parameter to get the next page of results.
        counts (dict): A dictionary to store the counts of keywords.

    Returns:
        None
    """
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    if not data:
        return

    posts = data.get('children', [])
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            word_lower = word.lower()
            count = title.split().count(word_lower)
            if count > 0:
                if word_lower in counts:
                    counts[word_lower] += count
                else:
                    counts[word_lower] = count

    after = data.get('after')
    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        if counts:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
