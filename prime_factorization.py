#!/usr/bin/python3
"""prime_factorization.py: Contains a function that
returns the prime factorization of a number"""


def prime_factorization(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num /= i
    if num > 2:
        factors.append(int(num))
    return factors


"""first_divisor.py: Contains a function that
returns the first divisor found for a number"""
def first_divisor(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return i
    return num
