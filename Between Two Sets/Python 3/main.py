#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(x, y):
    """Compute the Greatest Common Divisor (GCD) of two numbers."""
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    """Compute the Least Common Multiple (LCM) of two numbers."""
    return x * y // gcd(x, y)

def getTotalX(a, b):
    # Find the LCM of all elements in list a
    lcm_total = a[0]
    for num in a[1:]:
        lcm_total = lcm(lcm_total, num)
    
    # Find the GCD of all elements in list b
    gcd_total = b[0]
    for num in b[1:]:
        gcd_total = gcd(gcd_total, num)
    
    # Count numbers that are multiples of the LCM and divisors of the GCD
    count = 0
    for i in range(lcm_total, gcd_total + 1, lcm_total):
        if gcd_total % i == 0:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
