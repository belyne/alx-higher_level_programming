#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib package
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", content.decode('utf-8'))
