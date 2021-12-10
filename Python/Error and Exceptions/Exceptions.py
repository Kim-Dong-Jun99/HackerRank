# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    try:
        query = list(map(int, input().split()))
        print(int(query[0] / query[1]))
    except ValueError as e1:
        print('Error Code: %s' % e1)
    except ZeroDivisionError as e2:
        print('Error Code: integer division or modulo by zero')
