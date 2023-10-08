#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new_string = ""
    j = 0
    for i in range(length):
        if my_string[i] == "\x43" or my_string[i] == "\x63":
            new_string = new_string[:(i - j)] + my_string[(i + 1):]
            j += 1
    return (new_string)
