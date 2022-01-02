#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    # print('nodes %s'%t_nodes)
    # print('edges %s'%t_edges)
    # print('from %s'%t_from)
    # print('to %s'%t_to)
    answer = 0
    graph = [[] for i in range(t_nodes + 1)]
    for i in range(t_edges):
        graph[t_from[i]].append(t_to[i])
        graph[t_to[i]].append(t_from[i])

    cur = 1
    stack = []
    treesize = [1 for i in range(t_nodes + 1)]
    visited = [0 for i in range(t_nodes + 1)]
    visited[1] = 1
    traveled = 1
    while stack != [] or traveled < t_nodes:
        canF = False
        for i in graph[cur]:
            if visited[i] == 0:
                visited[i] = 1
                traveled += 1
                stack.append(cur)
                cur = i
                canF = True
                break
        if canF == False:
            treesize[stack[len(stack) - 1]] += treesize[cur]
            cur = stack.pop()
    # print(treesize)
    for i in treesize:
        if i % 2 == 0:
            answer += 1
    return answer - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
