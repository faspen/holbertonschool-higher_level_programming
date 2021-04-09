#!/usr/bin/python3
"""Task 6 module"""


import requests
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        value = {"email": sys.argv[2]}
        r = requests.post(url, data=value)
        print(r.text)
    except Exception as error:
        pass
