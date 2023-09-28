#!/bin/bash
# This script sends a GET request to a URL and displays the body if the response status code is 200

curl -s -X GET "$1" -i | grep "HTTP/1.0 200 OK" -q && curl -s -X GET "$1"
