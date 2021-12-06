# Enter your code here. Read input from STDIN. Print output to STDOUT
testCase = int(input())
for i in range(testCase):
    n = int(input())
    A = set(map(int,input().split()))
    m = int(input())
    B = set(map(int,input().split()))
    if A == B.intersection(A):
        print(True)
    else:
        print(False)