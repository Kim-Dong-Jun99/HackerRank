# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
query = list(input().split())
result = []
for i in list(permutations(list(query[0]), int(query[1]))):
    # print(i)
    temp = ''
    for j in list(i):
        temp += j
    result.append(temp)
result.sort()
for i in result:
    print(i)