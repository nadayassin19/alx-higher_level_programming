#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    mult_two = []
    for i in range(length):
        if my_list[i] % 2 == 0:
            mult_two.append(True)
        else:
            mult_two.append(False)
    return (mult_two)
