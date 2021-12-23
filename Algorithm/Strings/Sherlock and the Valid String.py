#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    setS = list(set(s))
    result = []
    for i in setS:
        result.append(s.count(i))
    if abs(min(result) - max(result)) == 0:
        return 'YES'
    elif result.count(1) == 1:
        if result.count(max(result)) == len(result) - 1:
            return 'YES'
        else:
            return 'NO'
    elif max(result) - min(result) == 1:
        if result.count(min(result)) == len(result)-1:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
