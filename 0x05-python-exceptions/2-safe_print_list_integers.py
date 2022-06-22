#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    e = a = 0
    while True:
        try:
            if e < x:
                print("{:d}".format(my_list[e]), end='')
                e += 1
                a += 1
            else:
                print()
                return a
        except( ValueError, TypeError):
            e += 1
