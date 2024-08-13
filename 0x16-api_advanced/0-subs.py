#!/usr/bin/python3
"""
Requesting subcribers count for a subreddit
from the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Args:
            subreddit(str): subreddit to be checked

    Returns:
            (int): Number of subscibers
    """

    url = f"https://api.reddit.com/r/{subreddit}/about"
    header = {'User-Agent': 'ubuntu by Frank'}
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        return 0
    return response.json().get('data', 0).get('subscribers', 0)
