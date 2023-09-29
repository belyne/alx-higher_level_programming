#!/usr/bin/python3
"""
Takes your GitHub credentials and uses the GitHub API to display your id
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = 'https://api.github.com/user'
response = requests.get(url, auth=(username, password))

try:
    data = response.json()
    if 'id' in data:
        print(data['id'])
    else:
        print("User ID not found in response")
except ValueError:
    print("None")
