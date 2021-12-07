#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    newPrice = price[:]
    newPrice.sort()
    values = {}
    for i in range(len(price)):
        values[price[i]] = i
    minimum = None
    for i in range(len(price)-1):
        if values[newPrice[i]] > values[newPrice[i+1]]:
            if minimum == None:
                minimum = newPrice[i+1] - newPrice[i]
            elif minimum > newPrice[i+1] - newPrice[i]:
                minimum = newPrice[i+1] - newPrice[i]
    return minimum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
