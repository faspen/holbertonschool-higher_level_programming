#!/usr/bin/python3
def safe_print_division(a, b):
    answer = None
    try:
        answer = a / b
        return answer
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(answer))
