import sys, math
input = sys.stdin.readline
a = 1000 - int(input())

ex1 = [500,100,50,10,5,1]

n = 0
for i in range(6):
    n += int(a/ex1[i])
    a = a%ex1[i]

print(n)