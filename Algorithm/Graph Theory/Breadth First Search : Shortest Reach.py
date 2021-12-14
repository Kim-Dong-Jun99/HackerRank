#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    graph = [[] for i in range(n + 1)]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    distances = {}
    result = []
    dis = 1
    nextNode = graph[s][:]
    prev = []
    while nextNode != []:
        temp = []
        for i in nextNode:
            if (i in prev) == False:
                prev += [i]
                temp += graph[i][:]
                distances[i] = (dis * 6)
        # prev += nextNode
        nextNode = temp
        dis += 1
    for i in range(1, n + 1):
        if i != s:
            if (i in distances):
                result.append(distances[i])
            else:
                result.append(-1)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
