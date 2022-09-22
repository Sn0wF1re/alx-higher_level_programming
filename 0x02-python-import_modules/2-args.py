#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1
    i = 1

    if count == 1:
        print("{} argument:".format(count))
    else:
        if count == 0:
            print("{} arguments.".format(count))
        else:
            print("{} arguments:".format(count))
    while i <= count:
        print("{}: {}".format(i, argv[i]))
        i += 1
