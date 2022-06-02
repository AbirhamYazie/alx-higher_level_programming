#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('0 arguments.')
        exit()
    arg_number = len(sys.argv) - 1
    if len(sys.argv) == 2:
        print('{} argument:'.format(arg_number))
    else:
        print('{} arguments:'.format(arg_number))

    count = 0
    for item in sys.argv:
        count = count + 1
        if count == 1:
            continue
        print('{}: {}'.format(count - 1, item))
