import sys
input = sys.stdin.readline
n = int(input())
ex = list(map(int, input().split()))

max = 1
x = 1
for i in range(n-1):
    if ex[i] <= ex[i+1]:
        x += 1
        if max < x:
            max = x
    else:
        x = 1

ex = ex[::-1]
y = 1    
for j in range(n-1):
    if ex[j] <= ex[j+1]:
        y += 1
        if max < y:
            max = y
    else:
        y = 1
            
print(max)