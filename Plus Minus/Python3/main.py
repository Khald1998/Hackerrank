#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Initialize counters for positive, negative, and zero elements
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Calculate the total number of elements
    total_elements = len(arr)

    # Iterate over the array and update the counters
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Calculate ratios and format them to 6 decimal places
    positive_ratio = positive_count / total_elements
    negative_ratio = negative_count / total_elements
    zero_ratio = zero_count / total_elements

    # Print the ratios
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
