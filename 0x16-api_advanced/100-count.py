#!/usr/bin/python3
"""
Generate a sorted count of given keywords contained
in the titles of all hot articles for a given subreddit
"""
from collections import defaultdict
import requests


def count_words(subreddit, word_list, keywords=None, after=None):
    """
    Queries the Reddit API and returns a sorted count of given keywords
    contained in the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): subreddit to be searched
        word_list (list): list of keywords to be searched
        keywords (dict): dictionary to store keyword counts
        after (str): the ID of the last item from the previous response

    Returns:
        dict: a dictionary with keywords and their respective counts
    """
    if keywords is None:
        keywords = defaultdict(int)

    url = f"https://api.reddit.com/r/{subreddit}/hot"
    header = {'User-Agent': 'ubuntu by Frank'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=header, params=params)
        response.raise_for_status()
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            post = post.get('data', {}).get('title').lower()
            title_words = post.split()

            for word in word_list:
                word = word.lower()
                if word in title_words:
                    keywords[word] += title_words.count(word)

        next_after = data.get('data', {}).get('after')
        if next_after:
            return count_words(subreddit, word_list, keywords, next_after)

    except requests.RequestException as e:
        pass

    sorted_keys = sorted(dict(keywords).items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_keys:
        print(f"{word}: {count}")

    return
