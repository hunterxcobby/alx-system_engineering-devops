#!/usr/bin/python3

"""
Query Reddit API for number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    Returns:
    - int: Number of subscribers, or 0 if the subreddit is invalid.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Ensure a custom User-Agent to prevent errors.
    headers = {'User-Agent': 'My User Agent'}

    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Parse response as JSON
        data = response.json()

        # Check if 'data' key exists and 'subscribers' key exists within it
        if 'data' in data and 'subscribers' in data['data']:
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # Return 0 if 'data' or 'subscribers' key doesn't exist
            return 0
    except Exception:
        # Return 0 if there's any exception during the request
        return 0
