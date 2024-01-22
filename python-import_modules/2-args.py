#!/usr/bin/python3
import sys
# python3 --version 
if __name__ == "__main__":
    argc = len(sys.argv)
    count = 1

    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1: {}".format(str(sys.argv[1])))
    else:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, str(sys.argv[i])))
