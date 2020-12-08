#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ltr = ord(c)
        if (97 <= ltr <= 122):
            ltr = ltr - 32
        print("{:c}".format(ltr), end='')
    print()
