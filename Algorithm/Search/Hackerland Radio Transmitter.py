#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()
    # temp = []
    # result = 0
    # for i in range(len(x)):
    #     if temp == []:
    #         temp.append(x[i])
    #     elif len(temp) == 1:
    #         if x[i] > temp[0]+k:
    #             if x[i-1] != temp[0] :
    #                 temp.append(x[i-1])
    #             else:
    #                 result += 1
    #                 temp = [x[i]]
    #     else:
    #         if x[i] > temp[1]+k:
    #             result += 1
    #             temp = [x[i]]
    #     # print('i = %d, temp = %s'%(i,temp))
    # return result+1
    i = 0
    result = 0
    while i < len(x):
        result += 1
        compare = x[i]
        while i < len(x) and x[i] <= compare + k:
            i += 1
        compare = x[i - 1]
        i -= 1
        while i < len(x) and x[i] <= compare + k:
            i += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
