#!/bin/python

import sys

def hans_deckers():
    """Print the Hans Deckers iteration. Arguments are positional arguments
    for the script"""
    argc = len(sys.argv)
    if argc < 3:
        exit("Not enough arguments")
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    lower = min(a, b)
    higher = max(a, b)
    for i in range(0, 1001):
        report(i, lower, higher)

def divides(a, b):
    """Return whether a divides b. In other terms: b is divisible by a"""
    return b % a == 0

def report(i, lower, higher):
    """Report i. Substitute message if divisible by lower, higher or both"""
    ld = divides(lower, i)
    hd = divides(higher, i)
    if ld and hd:
        print("HANS DEKKERS")
    elif ld:
        print("HANS")
    elif hd:
        print("DEKKERS")
    else:
        print(i)

if __name__ == "__main__":
    hans_deckers()
