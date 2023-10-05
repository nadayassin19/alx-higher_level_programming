#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = (len(sys.argv)) - 1
    if i == 0:
        print("0 arguments")
    elif i == 1:
        print("1 argument")
    else:
        print("{} argument".format(i))
    if i >= 1:
        i = 0
        for arg in range(len(sys.argv)):
            if i != 0:
                print("{}: {}".format(i, arg))
            i = i + 1
