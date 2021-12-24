#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    sumL = sum(arr[0:0])
    sumR = sum(arr[1:])
    for i in range(len(arr)):
        if sumL == sumR:
            return 'YES'
        elif i == len(arr)-1:
            return 'NO'
        else:
            sumL += arr[i]
            sumR -= arr[i+1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
