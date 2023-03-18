import sys
input = sys.stdin.readline
a = int(input())

ex1 = [300,60,10]

if a%10 == 0:
    n = []
    for i in range(3):
        n.append(int(a/ex1[i]))
        a = a%ex1[i]
    print(*n)
    
else:
    print(-1)