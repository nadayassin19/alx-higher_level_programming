#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        req_tuple = (length, None)
    else:
        req_tuple = (length, sentence[0])
    return (req_tuple)
