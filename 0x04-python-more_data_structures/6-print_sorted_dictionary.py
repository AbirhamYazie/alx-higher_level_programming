#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mat = sorted(a_dictionary)
    for item in mat:
        print('{}: {}'.format(item, a_dictionary[item]))


