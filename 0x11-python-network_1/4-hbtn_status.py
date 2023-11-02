#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests package
"""

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
content = response.text

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)