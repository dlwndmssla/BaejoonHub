import sys
input = sys.stdin.readline
n = int(input())
coffee = []
for i in range(n):
    a = int(input())
    coffee.append(a)

coffee = sorted(coffee)[::-1]
k = 0
for i in range(n):
    b = coffee[i]-i
    if b> 0:
        k += b
    
print(k)