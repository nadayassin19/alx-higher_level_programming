#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    new_list = []
    for i in range(length):
        new_list.append(my_list[length - (i + 1)])
        print("{:d}".format(new_list[i]))
