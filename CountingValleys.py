#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valleys = 0
    in_valley = False
    
    for step in path:
        if step == 'U':
            altitude += 1
        else:
            altitude -= 1
        
        if altitude < 0:
            in_valley = True
        elif altitude == 0 and in_valley:
            valleys += 1
            in_valley = False
    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
