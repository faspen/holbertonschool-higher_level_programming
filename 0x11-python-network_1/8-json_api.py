#!/usr/bin/python3
"""Task 8 module"""


import requests
import sys


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        data = r.json()
        if not data:
            print('No result')
        else:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
    except Exception:
        print('Not a valid JSON')
