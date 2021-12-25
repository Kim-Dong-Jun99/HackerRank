#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    result = 0
    if int((a ** (1/2))) - (a ** (1/2)) == 0:
        start = int((a ** (1/2)))
    else:
        start = int((a ** (1/2))) + 1
    # for i in range(a,b+1):
    #     temp = i **(1/2)
    #     if temp - int(temp) == 0:
    #         result += 1
    while True:
        if start ** 2 >= a and start ** 2 <= b:
            result +=1
            start += 1
        else:
            break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
