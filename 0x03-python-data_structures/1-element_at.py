#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx > length:
        return (None)
    else:
        for i in range (length):
            return(my_list[idx])
