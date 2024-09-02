#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the given integer n. If n is 0, returns 1 as 0! is defined to be 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read an integer from command-line arguments, compute its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)