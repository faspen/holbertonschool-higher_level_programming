#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for thingy in names:
        if (thingy[0] != '_'):
            print(thingy)
