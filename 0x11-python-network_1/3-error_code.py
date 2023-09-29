#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the response body or an error code
"""

import urllib.request
import urllib.error
import sys

url = sys.argv[1]

request = urllib.request.Request(url)

try:
    with urllib.request.urlopen(request) as response:
        content = response.read()
    print(content.decode("ascii"))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
