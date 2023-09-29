#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays
the response body or an error code if >= 400
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
