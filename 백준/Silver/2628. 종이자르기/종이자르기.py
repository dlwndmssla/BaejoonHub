import sys, math
input = sys.stdin.readline
x = [0]
y = [0]
N,M = map(int, input().split())
for i in range(int(input())):
    a,b = map(int, input().split())
    if a == 0:
        x.append(b)
    else:
        y.append(b)

x.append(M)
y.append(N)
x.sort()
y.sort()
max_x = 0
max_y = 0
for i in range(1, len(x)):
    if max_x < x[i]-x[i-1]:
        max_x = x[i]-x[i-1]
      
for j in range(1, len(y)):
    if max_y < y[j]-y[j-1]:
        max_y = y[j]-y[j-1]
        
print(max_x*max_y)