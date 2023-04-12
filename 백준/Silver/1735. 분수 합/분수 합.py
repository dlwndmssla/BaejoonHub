import sys
input = sys.stdin.readline
a,b = map(int, input().split())
c,d = map(int, input().split())

x = (a*d+b*c)
y = (d*b)

for i in range(min(x,y),0,-1):
    if x%i == y%i == 0:
        break

print(int(x/i),int(y/i))