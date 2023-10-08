#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    new_list = []
    if idx < 0 or idx > (length - 1):
        return(my_list)
    else:
        for i in range(length):
            if i != idx:
                new_list.append(my_list[i])
        return (new_list)
