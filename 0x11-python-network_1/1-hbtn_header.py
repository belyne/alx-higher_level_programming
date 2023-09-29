#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the value of X-Request-Id variable in the header
"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')

print(header)
