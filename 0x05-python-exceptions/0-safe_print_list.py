#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    e = 0
    while True:
        try:
            if e < x:
                print(my_list[e], end='')
                e +=1
            else:
                print()
                return e
        except IndexError:
            print()
            return e
