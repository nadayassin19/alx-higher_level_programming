#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    for i in range(len(str)):
        if i != n:
            ch = ch + str[i]
    return (ch)
