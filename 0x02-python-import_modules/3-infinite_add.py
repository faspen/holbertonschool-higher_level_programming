#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arglen = len(sys.argv)
    res = 0

    if arglen == 1:
        print("0")
    elif arglen == 2:
        print("{}".format(int(sys.argv[1])))
    else:
        for i in range(1, arglen):
            res += int(sys.argv[i])
        print("{}".format(res))
