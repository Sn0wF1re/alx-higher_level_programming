#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = 0
    count = len(argv) - 1
    i = 1

    while i <= count:
        result += int(argv[i])
        i += 1
    print(result)
