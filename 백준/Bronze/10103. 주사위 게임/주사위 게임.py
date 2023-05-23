import sys
#input = sys.stdin.readline
n = int(input())
a = 100
b = 100

for i in range(n):
    x,y = map(int, input().split())
    if x == y:
        continue
    elif x > y:
        b -= x
    else:
        a -= y
print(a)
print(b)