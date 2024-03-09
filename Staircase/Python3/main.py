#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    count = 1
    for i in range(n):
        for j in range(n):
            if(j>=n-count):
                print('#',end='')
            else:
                print(' ',end='')
        count=count+1 
        print("\n",end='')

            


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
