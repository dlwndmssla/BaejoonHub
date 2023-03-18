import sys
input = sys.stdin.readline
ex1 = []
a = int(input())
for i in range(a):
    ex1.append(int(input()))
    
ex1.sort()
ex1 = ex1[::-1]
ex2 = []
for i in range(a):
    ex2.append((i+1)*ex1[i])
    
print(max(ex2))