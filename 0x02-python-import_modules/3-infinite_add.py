#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    summation = 0

    for x in range(1, len(sys.argv)):
        number = int(sys.argv[x])
        summation += number
    print("{}".format(summation))
