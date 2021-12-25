#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    longestLength = 0
    stan = 0
    tempLength = 0
    for i in a:
        if stan == 0:
            stan = i
            tempLength += 1
        else:
            if i - stan <= 1:
                tempLength += 1
            else:
                if longestLength < tempLength:
                    longestLength = tempLength
                    tempLength = 1
                    stan = i
                else:
                    tempLength = 1
                    stan = i

    if longestLength < tempLength:
        longestLength = tempLength

    return longestLength


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
