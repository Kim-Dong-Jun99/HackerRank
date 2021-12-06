#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    zero = 0
    minus = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            minus += 1
        else :
            zero += 1
    print('%0.6f'%(positive/len(arr)))
    print('%0.6f'%(minus/len(arr)))
    print('%0.6f'%(zero/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
