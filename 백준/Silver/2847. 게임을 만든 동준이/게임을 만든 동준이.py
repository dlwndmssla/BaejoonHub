import sys
input=sys.stdin.readline
n = int(input())
level = []

for i in range(n):
    a = int(input())
    level.append(a)
    
level = level[::-1]
k = 0
for j in range(1,n):
    if level[j-1] <= level[j]:
        x = level[j-1]-1
        k += level[j]-x
        level[j] = x
        
print(k)