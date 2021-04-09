#!/usr/bin/python3
"""Task 1 module"""


from sys import argv
from urllib import request


if __name__ == "__main__":
    url = argv[1]

    req = request.Request(url)
    with request.urlopen(req) as response:
        print((response.headers).get("X-Request-Id"))
