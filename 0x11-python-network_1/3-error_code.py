#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the response body or an error code
"""

import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
    print(content.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
