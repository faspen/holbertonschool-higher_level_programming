#!/usr/bin/python3
for a in range(122, 96, -1):
    if a % 2 == 0:
        print("{:c}".format(a), end='')
    else:
        print("{:c}".format(a - 32), end='')
