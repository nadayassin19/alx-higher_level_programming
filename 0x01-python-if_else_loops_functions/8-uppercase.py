#!/usr/bin/python3
def uppercase(ch):
    for i in range(len(ch)):
        asc = ord(ch[i])
        if asc > 96 and asc < 123:
            num = 32
        else:
            num = 0
        print("{0:c}".format(asc - num), end="")
print("\n")
