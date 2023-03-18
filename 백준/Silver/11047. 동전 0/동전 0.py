import sys, math
input = sys.stdin.readline
a,b = map(int, input().split())
ex1 = []

for i in range(a):
    ex1.append(int(input()))
    
ex1 = ex1[::-1]
n = 0
for i in range(a):
    n += int(b/ex1[i])
    b = b%ex1[i]

print(n)