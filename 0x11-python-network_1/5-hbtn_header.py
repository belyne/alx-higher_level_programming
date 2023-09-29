#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the value of X-Request-Id in the response header
"""

import requests
import sys

url = sys.argv[1]

response = requests.get(url)
header = response.headers['X-Request-Id']

print(header)
