#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(15000)


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    # Write your code here
    indexes.insert(0, [0, 0])
    result = [[] for i in range(len(queries))]
    index = 0
    for i in queries:
        swap(indexes, 1, 1, i, result[index])
        index += 1

    return result


def swap(indexes, node, depth, k, result):
    if depth % k == 0:
        indexes[node][0], indexes[node][1] = indexes[node][1], indexes[node][0]
    if indexes[node][0] != -1:
        swap(indexes, indexes[node][0], depth + 1, k, result)
    result.append(node)
    if indexes[node][1] != -1:
        swap(indexes, indexes[node][1], depth + 1, k, result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
