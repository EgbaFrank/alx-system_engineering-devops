#!/usr/bin/python3
"""
prints the titles of the first 10
hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Args:
        subreddit (str): subreddit to be searched
    Return:
        (str): titles of the 10 ten posts
    """
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    header = {'User-Agent': 'ubuntu by Frank'}
    response = requests.get(url, headers=header, params={'limit': 10})

    if response.status_code == 200:
        posts = response.json().get('data').get('children')

        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
