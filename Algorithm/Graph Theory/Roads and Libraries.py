#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    graph = [[] for i in range(n + 1)]
    for i in cities:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    searched = set()
    group = []
    for i in range(1, n + 1):
        if graph[i] != [] and (i in searched) == False:
            visited = [i]
            nextCity = graph[i][:]
            visited += nextCity
            searched.add(i)
            while nextCity:
                temp = []
                for j in nextCity:
                    searched.add(j)
                    for k in graph[j]:
                        if (k in visited) == False:
                            visited.append(k)
                            temp.append(k)
                nextCity = temp

            group.append(visited)
        elif graph[i] == []:
            group.append([i])
    result = 0
    # print('group = %s'%group)
    if c_lib < c_road:
        return c_lib * n
    else:
        for i in group:
            result += (len(i) - 1) * c_road + c_lib

        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
