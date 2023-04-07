import sys
input = sys.stdin.readline
n,m = map(int, input().split())
egg = []
for i in range(m):
    egg.append(int(input()))
    
egg = sorted(egg)[::-1]
revenue = []
for i in range(1,min(n,m)+1):
    revenue.append(i*egg[i-1])
    
k = max(revenue)
print(egg[revenue.index(k)],k)