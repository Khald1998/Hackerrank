#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum = 0
    min = 999999999999999
    max = 0

    for value in arr:
            sum += value
            if value < min:
                min = value
            
            if value > max:
                max = value
            
    miniSum = sum - max
    maxiSum = sum - min

    print(miniSum , maxiSum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
