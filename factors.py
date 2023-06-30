#!/usr/bin/python3
import sys


"""first_divisor.py: Contains a function that
returns the first divisor found for a number"""


def first_divisor(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return i
    return num
