#!/usr/bin/python3
"""
Takes a letter, sends a POST request to
http://0.0.0.0:5000/search_user, and displays the response
"""

import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
payload = {'q': q}

response = requests.post(url, data=payload)

try:
    json_data = response.json()
    if json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
