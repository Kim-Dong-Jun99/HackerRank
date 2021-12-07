# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int ,input().split()))
n = int(input())
check = True
for i in range(n):
    temp = set(map(int, input().split()))
    if A == temp or A.intersection(temp) != temp:
        check = False
        print(False)
        break
if check:
    print(True)