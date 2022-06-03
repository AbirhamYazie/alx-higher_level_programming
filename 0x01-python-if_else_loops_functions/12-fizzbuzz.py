#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num == 3*num:
            print('Fizz', end=' ')
        elif num == 5*num:
            print('Buzz', end=' ')
        elif num == 3*num and num == 5*num:
            print('FizzBuzz', end=' ')
        else:
            print(num, end=' ')
