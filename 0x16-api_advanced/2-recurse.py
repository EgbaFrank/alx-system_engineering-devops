#!/usr/bin/python3
"""
Generate a list containing the titles
of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Args:
        subreddit (str): subreddit to be searched
        hot_list (list): list of hot artiles titles
        after (str): the ID of the last item from the previous response

    Return:
        (list): titles of all hot posts
    """
    if not after:
        url = f"https://api.reddit.com/r/{subreddit}/hot"
    else:
        url = f"https://api.reddit.com/r/{subreddit}/hot?after={after}"

    header = {'User-Agent': 'ubuntu by Frank'}
    response = requests.get(url, headers=header, params={'limit': 100})

    try:
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if not posts:
                return hot_list

            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))

            next_after = data.get('data', {}).get('after')
            if not next_after:
                return hot_list

            recurse(subreddit, hot_list, next_after)
        else:
            return None

    except Exception as e:
        print(e)

    return None
