import sys
input = sys.stdin.readline
n = int(input())

ex = list()
for i in range(n):
    ex.append(list(map(int,input().split())))
    
ex.sort(key=lambda x : (x[0], x[1]) )
for i in range(n):
    print(*ex[i])