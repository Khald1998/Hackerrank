#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract the hour and convert to integer
    hour = int(s[:2])
    
    # Process for AM
    if s[-2:].upper() == 'AM':
        # Convert '12' AM to '00'
        if hour == 12:
            return '00' + s[2:-2]
        else:
            return s[:-2]
    
    # Process for PM
    else:
        # Convert '12' PM to '12'
        if hour != 12:
            hour += 12
        return str(hour).zfill(2) + s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
