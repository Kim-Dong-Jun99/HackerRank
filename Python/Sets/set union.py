# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(list(map(int , input().split())))
m = int(input())
french = set(list(map(int, input().split())))
print(len(english.union(french)))