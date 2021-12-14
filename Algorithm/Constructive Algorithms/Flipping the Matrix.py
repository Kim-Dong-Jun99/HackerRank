#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = int(len(matrix)/2)
    size = len(matrix)-1
    compare = [[0,0],[0,-size],[-size,0],[-size,-size]]
    result = 0
    for i in range(n):
        for j in range(n):
            temp = []
            for k in compare:
                temp.append(matrix[abs(i+k[0])][abs(j+k[1])])
            result += max(temp)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
