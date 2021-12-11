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
    maxScore = scores[0]
    minScore = scores[0]
    countMax = 0
    countMin = 0
    for i in range(1, len(scores)):
        if scores[i] > maxScore:
            countMax += 1
            maxScore = scores[i]
        elif scores[i] < minScore:
            countMin += 1
            minScore = scores[i]

    return [countMax, countMin]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
