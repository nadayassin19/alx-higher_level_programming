#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        sentence[0] = "None"
        req_tuple = (length, sentence[0])
    else:
        req_tuple = (length, sentence[0])
    return (req_tuple)
