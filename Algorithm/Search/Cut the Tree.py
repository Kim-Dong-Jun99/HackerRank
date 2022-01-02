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
    print(sum(data))
    data.insert(0, 0)
    graph = [[] for j in range(len(data))]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    visited = [0 for i in range(len(data))]
    cur = 1
    visited[1] = 1
    stack = []
    traveled = 1

    while traveled < len(data) - 1 or stack != []:

        canF = False
        for i in graph[cur]:

            if visited[i] == 0:
                stack.append(cur)
                visited[i] = 1
                cur = i
                traveled += 1
                canF = True
                break
        if canF == False:
            data[stack[len(stack) - 1]] += data[cur]
            cur = stack.pop()
            # if stack == []:
            #     break

    totalSum = data[1]
    print(totalSum)
    minDiff = None
    revisit = [0 for i in range(len(data))]
    cur = 1
    revisit[1] = 1
    traveled = 1
    while stack != [] or traveled < len(data) - 1:
        canF = False
        for i in graph[cur]:
            if revisit[i] == 0:
                temp = abs(totalSum - data[i] - data[i])
                if minDiff == None:
                    minDiff = temp
                elif minDiff > temp:
                    minDiff = temp
                stack.append(cur)
                traveled += 1
                revisit[i] = 1
                cur = i
                canF = True
                break
        if canF == False:
            cur = stack.pop()
            # if stack == []:
            #     break
    return minDiff


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
