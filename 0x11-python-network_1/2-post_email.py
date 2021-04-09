#!/usr/bin/python3
"""Task 2 module"""


from sys import argv
import urllib.parse
import urllib.request


url = argv[1]
value = {"email": argv[2]}
data = urllib.parse.urlencode(value)
data = data.encode('ascii')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    html = response.read().decode("utf-8")
