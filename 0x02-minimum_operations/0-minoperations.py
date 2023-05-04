#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in the file. """
    if n <= 1:
        return 0
    num_operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            num_operations += divisor
            n /= divisor
        divisor += 1
    return num_operations
