#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightlOnAChessboard(n):
    # Write your code here
    result = [[0 for i in range(n - 1)] for j in range(n - 1)]
    for i in range(1, n):
        for j in range(i + 1):
            times = 0
            nextNode = [[0, 0]]
            prev = []
            success = False
            while nextNode != []:
                temp = []
                for k in nextNode:
                    if k[0] - i >= 0 and k[1] - j >= 0 and ([k[0] - i, k[1] - j] in temp) == False and (
                            [k[0] - i, k[1] - j] in prev) == False:
                        temp.append([k[0] - i, k[1] - j])
                    if k[0] - i >= 0 and k[1] + j < n and ([k[0] - i, k[1] + j] in temp) == False and (
                            [k[0] - i, k[1] + j] in prev) == False:
                        temp.append([k[0] - i, k[1] + j])
                    if k[0] + i < n and k[1] - j >= 0 and ([k[0] + i, k[1] - j] in temp) == False and (
                            [k[0] + i, k[1] - j] in prev) == False:
                        temp.append([k[0] + i, k[1] - j])
                    if k[0] + i < n and k[1] + j < n and ([k[0] + i, k[1] + j] in temp) == False and (
                            [k[0] + i, k[1] + j] in prev) == False:
                        temp.append([k[0] + i, k[1] + j])
                    if k[0] - j >= 0 and k[1] - i >= 0 and ([k[0] - j, k[1] - i] in temp) == False and (
                            [k[0] - j, k[1] - i] in prev) == False:
                        temp.append([k[0] - j, k[1] - i])
                    if k[0] - j >= 0 and k[1] + i < n and ([k[0] - j, k[1] + i] in temp) == False and (
                            [k[0] - j, k[1] + i] in prev) == False:
                        temp.append([k[0] - j, k[1] + i])
                    if k[0] + j < n and k[1] - i >= 0 and ([k[0] + j, k[1] - i] in temp) == False and (
                            [k[0] + j, k[1] - i] in prev) == False:
                        temp.append([k[0] + j, k[1] - i])
                    if k[0] + j < n and k[1] + i < n and ([k[0] + j, k[1] + i] in temp) == False and (
                            [k[0] + j, k[1] + i] in prev) == False:
                        temp.append([k[0] + j, k[1] + i])
                prev += nextNode
                nextNode = temp[:]
                times += 1
                if ([n - 1, n - 1] in nextNode):
                    success = True
                    break
            if success:
                result[i - 1][j - 1] = times
                result[j - 1][i - 1] = times
            else:
                result[i - 1][j - 1] = -1
                result[j - 1][i - 1] = -1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
