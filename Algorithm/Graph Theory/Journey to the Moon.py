#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#


def journeyToMoon(n, astronaut):
    # Write your code here
    graph = [[] for i in range(n)]
    for i in astronaut:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    searched = []
    result = []
    i = 0
    answer = 0
    while i < n:
        if graph[i] != [] and (i in searched) == False:
            visited = set()
            visited.add(i)
            nextV = graph[i][:]
            while nextV:
                temp = []
                for j in nextV:
                    visited.add(j)
                    for k in graph[j]:
                        if (k in visited) == False:
                            temp.append(k)
                nextV = temp
            # print('v = %s'%visited)
            searched += list(visited)
            result.append(len(visited))
        elif graph[i] == []:
            result.append(1)
        i += 1

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            answer += result[i] * result[j]

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
