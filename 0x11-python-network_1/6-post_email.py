#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request, and displays the response body
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}

response = requests.post(url, data=payload)
content = response.text

print("Your email is:", email)
