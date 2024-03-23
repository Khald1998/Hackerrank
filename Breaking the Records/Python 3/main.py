#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    Maximum = scores[0]
    Minimum = scores[0]
    Count_min = 0
    Count_max = 0
    for x in scores[1:]:
        if x>Maximum:
            Count_max+=1
            Maximum=x
        elif x<Minimum:
            Count_min+=1
            Minimum=x
    return Count_max,Count_min
        
        
            
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
