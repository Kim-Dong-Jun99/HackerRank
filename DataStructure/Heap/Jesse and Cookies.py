#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    heap = [-1]
    for i in A:
        heap.append(i)
        parent = int((len(heap) - 1) / 2)
        child = len(heap) - 1

        while parent > 0:
            if heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
                parent = int(parent / 2)
            else:
                break
    result = 0
    while heap[1] <= k:
        temp = []
        for j in range(2):
            if len(heap) == 2:
                if heap[1] < k:
                    return -1
            elif len(heap) == 3:
                if k > heap[1] + heap[2] * 2:
                    return -1
                else:
                    return result + 1
            else:
                heap[1], heap[len(heap) - 1] = heap[len(heap) - 1], heap[1]
                temp.append(heap.pop())
                parent = 1
                lchild = 2
                rchild = 3
                while rchild < len(heap) or lchild < len(heap):
                    if rchild < len(heap):
                        if heap[parent] > min(heap[rchild], heap[lchild]):
                            if heap[rchild] < heap[lchild]:
                                heap[parent], heap[rchild] = heap[rchild], heap[parent]
                                parent = rchild
                                lchild = parent * 2
                                rchild = parent * 2 + 1
                            else:
                                heap[parent], heap[lchild] = heap[lchild], heap[parent]
                                parent = lchild
                                lchild = parent * 2
                                rchild = parent * 2 + 1
                        else:
                            break
                    else:
                        if heap[parent] > heap[lchild]:
                            heap[parent], heap[lchild] = heap[lchild], heap[parent]
                            parent = lchild
                            lchild = parent * 2
                            rchild = parent * 2 + 1
                        else:
                            break
        val = temp[0] + temp[1] * 2
        heap.append(val)
        parent = int((len(heap) - 1) / 2)
        child = len(heap) - 1

        while parent > 0:
            if heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
                parent = int(parent / 2)
            else:
                break
        result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
