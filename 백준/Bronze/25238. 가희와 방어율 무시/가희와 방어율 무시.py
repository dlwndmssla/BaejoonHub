import sys
input = sys.stdin.readline
a,b = map(int, input().split())

x = a- a*b*0.01

if x >= 100:
    print(0)
else:
    print(1)