#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = number % -10
print(f"Last digit of {number} is {lastDigit}", end=" ")
if lastDigit > 5:
    print(f"and is greater than 5")
elif lastDigit == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
