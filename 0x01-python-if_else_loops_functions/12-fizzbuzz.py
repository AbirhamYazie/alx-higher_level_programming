#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            print('fizz', end=' ')
        elif n % 5 == 0:
            print('buzz', end=' ')
        elif n % 15 == 0:
            print('fizzbuzz', end=' ')
        else:
            print(n, end=' ')
