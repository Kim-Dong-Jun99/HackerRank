#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    result = recur(n*k)
    if result != 0:
        return result
    else:
        9
    # result = int(n)*k%9
    # if result == 0:
    #     return 9
    # else:
    #     return result
def recur(n):
    if len(n) == 1:
        return int(n)
    else:
        temp = 0
        for i in n:
            temp += int(i)%9
        return recur(str(temp))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
