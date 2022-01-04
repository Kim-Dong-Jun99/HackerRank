#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    # Write your code here
    graph = [start]
    result = 0
    end = [[] for i in range(n+1)]
    weights = [[] for i in range(n+1)]
    for i in edges:
        j = 0
        while j < len(weights[i[0]]):
            if i[2] < weights[i[0]][j]:
                break
            else:
                j += 1
        end[i[0]].insert(j,i[1])
        weights[i[0]].insert(j,i[2])
        k = 0
        while k < len(weights[i[1]]):
            if i[2] < weights[i[1]][k]:
                break
            else:
                k += 1
        end[i[1]].insert(k,i[0])
        weights[i[1]].insert(k,i[2])
    print(weights)
    print(end)
    while len(graph) < n:
        minWeight = None
        minWEnd = None
        minI = None
        for i in graph:
            if weights[i] != []:
                if minWeight == None:
                    minWeight = weights[i][0]
                    minWEnd = end[i][0]
                    minI = i
                else:
                    if weights[i][0] < minWeight:
                        minWeight = weights[i][0]
                        minWEnd = end[i][0]
                        minI = i
        if (minWEnd not in graph):
            graph.append(minWEnd)
            result += minWeight
        end[minI].pop(0)
        weights[minI].pop(0)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
