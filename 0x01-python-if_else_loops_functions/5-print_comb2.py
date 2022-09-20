#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("{:0>2}".format(number), end="\n")
    else:
        print("{:0>2}".format(number), end=", ",)
