#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    mst = []
    result = 0
    while g_weight:
        tempMin = min(g_weight)
        index = g_weight.index(tempMin)

        if mst == []:
            temp = set()
            temp.add(g_from[index])
            temp.add(g_to[index])
            mst.append(temp)
            result += tempMin
        else:
            check = False
            for i in range(len(mst)):
                if (g_from[index] in mst[i]):
                    check = True
                    if (g_to[index] in mst[i]):
                        break
                    else:
                        inserted = False
                        for j in range(len(mst)):
                            if (g_to[index] in mst[j]):
                                mst[i] = mst[i].union(mst[j])
                                result += tempMin
                                mst.pop(j)
                                inserted = True
                                break
                        if inserted == False:
                            mst[i].add(g_to[index])
                            result += tempMin
                    break
                elif (g_to[index] in mst[i]):
                    check = True
                    if (g_from[index] in mst[i]):
                        break
                    else:
                        inserted = False
                        for j in range(len(mst)):
                            if (g_from[index] in mst[j]):
                                mst[i] = mst[i].union(mst[j])
                                result += tempMin
                                mst.pop(j)
                                inserted = True
                                break
                        if inserted == False:
                            mst[i].add(g_from[index])
                            result += tempMin
                    break
            if check == False:
                temp = set()
                temp.add(g_from[index])
                temp.add(g_to[index])
                mst.append(temp)
                result += tempMin
        g_from.pop(index)
        g_to.pop(index)
        g_weight.pop(index)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res) + '\n')
    fptr.close()
