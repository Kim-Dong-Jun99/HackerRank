# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stan = set(map(int, input().split()))
m = int(input())
for i in range(m):
    query = list(input().split())
    temp = set(map(int, input().split()))
    if query[0] == 'intersection_update':
        stan.intersection_update(temp)
    elif query[0] == 'symmetric_difference_update':
        stan.symmetric_difference_update(temp)
    elif query[0] == 'difference_update':
        stan.difference_update(temp)
    else:
        stan.update(temp)
print(sum(list(stan)))