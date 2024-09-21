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
    # Write your code here
    min_val = scores[0]
    max_val = scores[0]
    min_count = 0
    max_count = 0
    
    for i in scores[1:]:
        if (i > max_val):
            max_val = i
            max_count +=1
        if (i < min_val):
            min_val = i
            min_count +=1
        
    return [max_count,min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
