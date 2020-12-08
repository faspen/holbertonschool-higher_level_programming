#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number >= 0):
    last = number % 10
else:
    last = number * -1
    last = last % 10
    last = last * -1

print("Last digit of {} is".format(number), end=' ')
if last > 5:
    print("{} and is greater than 5".format(last))
elif last == 0:
    print("0 and is 0")
else:
    print("{} and is less than 6 and not 0".format(last))
