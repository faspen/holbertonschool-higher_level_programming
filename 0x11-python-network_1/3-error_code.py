#!/usr/bin/python3
"""Task 3 module"""


from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
	    resp = response.read()
            print(resp.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
