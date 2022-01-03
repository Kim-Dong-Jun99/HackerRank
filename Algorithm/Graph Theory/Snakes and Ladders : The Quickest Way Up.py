#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    # Write your code here
    nextV = set()
    visited = set()
    nextV.add(1)
    ladderStart = [ladders[i][0] for i in range(len(ladders))]
    ladderEnd = [ladders[i][1] for i in range(len(ladders))]
    snakesStart = [snakes[i][0] for i in range(len(snakes))]
    snakesEnd = [snakes[i][1] for i in range(len(snakes))]
    turn = 0
    while (100 not in nextV) and len(nextV) != 0:
        temp = set()
        for i in nextV:
            for j in range(1, 7):
                if ((i + j) not in visited):
                    if ((i + j) not in ladderStart) and ((i + j) not in snakesStart):
                        temp.add(i + j)
                        visited.add(i + j)
                    else:
                        if ((i + j) in ladderStart):
                            temp.add(ladderEnd[ladderStart.index(i + j)])
                            visited.add(ladderEnd[ladderStart.index(i + j)])
                        else:
                            temp.add(snakesEnd[snakesStart.index(i + j)])
                            visited.add(snakesEnd[snakesStart.index(i + j)])
        nextV = temp
        turn += 1

    if len(nextV) == 0:
        return -1
    return turn


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
