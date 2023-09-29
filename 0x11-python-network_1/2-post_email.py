#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request, and displays the response body
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    content = response.read()

print("Your email is:", email)
