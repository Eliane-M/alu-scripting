#!/usr/bin/python3
"""
prints the titles of 
the first 10 hot posts listed 
for a given subreddit.
"""


import json
import requests
import sys

def top_ten(subreddit):
    """
    prints 10 hot posts
    """
    URL = f"https/
