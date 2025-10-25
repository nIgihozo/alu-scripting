#!/usr/bin/python3
""" Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'limit': 10}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    
    response = requests.get(
        subreddit_url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        json_data = response.json()
        
        # Check if the "children" list exists and has content (a final check)
        posts = json_data.get('data', {}).get('children', [])
        
        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except (requests.exceptions.JSONDecodeError, AttributeError):
        # Handle cases where the response is not valid JSON or the structure is unexpected
        print(None)
