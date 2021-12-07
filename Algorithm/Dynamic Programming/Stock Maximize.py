#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    maxProfit = 0
    temp = []
    tempMax = max(prices)
    for i in range(len(prices)):
        if prices[i] == tempMax:
            maxProfit += tempMax * len(temp) - sum(temp)
            temp = []
            if i != len(prices) - 1:
                tempMax = max(prices[i + 1:])
        else:
            temp.append(prices[i])

    return maxProfit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
