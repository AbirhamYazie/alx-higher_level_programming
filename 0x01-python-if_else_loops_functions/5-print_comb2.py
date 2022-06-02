#!/usr/bin/python3
for item in range(99):
    print("{:02d}".format(item), end=", ")
else:
    print("{:02d}".format(item + 1))
