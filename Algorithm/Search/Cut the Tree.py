#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    # Write your code here
    graph = [[] for j in range(len(data) + 1)]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    level = [0 for i in range(len(data) + 1)]
    init = 1
    nextV = [1]
    visited = [0 for i in range(len(data) + 1)]
    totalSum = 0
    while nextV:
        temp = []
        for i in nextV:
            level[i] = init
            visited[i] = 1
            totalSum += data[i - 1]
            for j in graph[i]:
                if visited[j] == 0:
                    temp.append(j)
        nextV = temp
        init += 1
    minDif = None
    # for i in edges:
    #     if level[i[0]] > level[i[1]]:
    #         nextV = [i[0]]
    #     else:
    #         nextV = [i[1]]
    #     tempSum = 0
    #     while nextV:
    #         temp = []
    #         for i in nextV:
    #             tempSum += data[i-1]
    #             for j in graph[i]:
    #                 if level[j] > level[i]:
    #                     temp.append(j)
    #         nextV = temp
    #     if minDif == None:
    #         minDif = abs(totalSum-tempSum - tempSum)
    #     else:
    #         if minDif > abs(totalSum-tempSum-tempSum):
    #             minDif = abs(totalSum-tempSum-tempSum)

    return minDif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
