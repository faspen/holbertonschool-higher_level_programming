#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arglen = len(sys.argv)

    if (arglen == 1):
        print("0 arguments.")
    elif (arglen == 2):
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arglen - 1))
        for j in range(1, arglen):
            print("{}: {}".format(j, sys.argv[j]))
