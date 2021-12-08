# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
query = list(map(list, input().split()))
result = []
for i in range(int(query[1][0])):
    con = []
    for j in list(combinations(query[0],i+1)):
        tempL = list(j)
        tempL.sort()
        temp = ''
        for k in tempL:
            temp += k
        con.append(temp)
    con.sort()
    result += con
for i in result:
    print(i)