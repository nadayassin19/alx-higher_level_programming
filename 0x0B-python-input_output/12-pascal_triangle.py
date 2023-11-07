#!/usr/bin/python3
"""a module pf a function that retrieve pascal triangle
"""

def pascal_triangle(n):
    """a function that returns a list of lists of integers
    representing the Pascal's triangle of n

    Args:
        n (int): base number of the pascal triangle
    """
    if n <= 0:
        return ([])

    main_list = []
    single_list = []

    for i in range(n):
        new_list = []
        p1 = 0
        p2 = -1
        for j in range(len(single_list) + 1):
            if p1 == len(single_list) or p2 == -1:
                new_list += [1]
            else:
                new_list += [single_list[p1] + single_list[p2]]
            p1 += 1
            p2 += 1
        main_list.append(new_list)
        single_list = new_list[:]

    return (main_list)
