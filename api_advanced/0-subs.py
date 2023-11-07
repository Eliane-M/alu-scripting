#!/usr/bin/python3
"""
uses reddit's APIs
to get the number of total number of subscribers
of a subrredit
"""


def number_of_subscribers(subreddit):
    import json
    import requests
    import sys

    subreddit = sys.argv[1]
    URL = f"https://www.reddit.com/r/subreddit/about.json"

    headers = {
            "User-Agent": "0-subs/1.0"
    }

    raw_response = requests.get(URL, headers=headers)
    json_response = raw_response.json()

    sub_count = json_response['data']['subscribers']

    print (sub_count)

if __name__ == "__main__":
    pass
