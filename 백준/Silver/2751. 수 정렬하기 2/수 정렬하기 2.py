import sys
input=sys.stdin.readline
a = []
b = int(input())

for i in range(b):
    a.append(int(input()))
    
a.sort()

for j in a:
    print(j)