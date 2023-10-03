#!/usr/bin/python3
def print_last_digit(number):
    lastDigit = number % 10
    print("{0:d}".format(lastDigit), end="")
    return (lastDigit)
