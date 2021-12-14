#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    # time = []
    # result = []
    # if orders == [[1,1],[1,1]]:
    #     return [1,2]
    # for i in orders:
    #     time.append(sum([i[0], i[1]]))
    # while True:
    #     temp = max(time)
    #     if temp == 0:
    #         break
    #     for i in range(time.count(temp)):
    #         index = time.index(temp)
    #         time[index] = 0
    #         result.append(index+1)
    # result.reverse()
    # return result
    dict = {}
    result = []
    ordertime = []
    for i in range(len(orders)):
        if (sum(orders[i]) in dict):
            temp = dict[sum(orders[i])][:]
            temp.append(i+1)
            dict[sum(orders[i])] = temp
        else:
            dict[sum(orders[i])] = [i+1]
        ordertime.append(sum(orders[i]))
    ordertime = list(set(ordertime))
    ordertime.sort()
    for i in ordertime:
        temp = dict[i][:]
        result += temp
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
