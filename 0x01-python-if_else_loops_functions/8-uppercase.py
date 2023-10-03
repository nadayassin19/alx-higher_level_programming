#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        asc = ord(str[i])
        if asc > 96 and asc < 123:
            num = 32
        else:
            num = 0
        print("{:c}".format(asc - num), end="")
    print("\n")
