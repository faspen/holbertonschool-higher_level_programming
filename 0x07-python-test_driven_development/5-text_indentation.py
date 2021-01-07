#!/usr/bin/python3
"""Module with text indent function"""


def text_indentation(text):
    """Indent text on certain chars
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    length = len(text)
    a = 0

    while a < length:
        if text[a] in ".?:":
            print("{:s}".format(text[a]), end="\n\n")
            while (a + 1) < length and ord(text[a + 1]) == 32:
                a += 1
        else:
            print("{:s}".format(text[a]), end="")
        a += 1
