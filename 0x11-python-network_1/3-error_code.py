#!/usr/bin/python3
"""Task 3 module"""


from sys import argv
from urllib import error
from urllib import request


if __name__ == "__main__":
    url = argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('ascii'))
    except error.URLError as e:
        print('Error code: {}'.format(e.code))
