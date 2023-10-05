#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    args = sys.argv
    for arg in args:
        if arg != args[0]:
            result += int(arg)
    print(result)
