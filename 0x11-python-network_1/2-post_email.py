#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request, and displays the response body
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
value = {"email": sys.argv[2]}
data = urllib.parse.urlencode(value).encode("ascii")

request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
